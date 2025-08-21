import asyncio
import websockets
import http.server
import socketserver
import threading
import traceback

# --- Configuration ---
HTTP_PORT = 8000
WEBSOCKET_PORT = 8765
# --- End Configuration ---

connected_clients = set()

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Live Text from Python</title>
    <style>
        body {{ font-family: sans-serif; background-color: #2b2b2b; color: #f1f1f1; }}
        #container {{ max-width: 800px; margin: 40px auto; padding: 20px; }}
        pre {{ 
            font-size: 2em; 
            white-space: pre-wrap; 
            word-wrap: break-word;
            background-color: #3c3f41;
            padding: 20px;
            border-radius: 8px;
            min-height: 100px;
        }}
    </style>
</head>
<body>
    <div id="container">
        <pre id="text-to-read">Waiting for text...</pre>
    </div>

    <script>
        const textElement = document.getElementById('text-to-read');
        const ws = new WebSocket('ws://localhost:{WEBSOCKET_PORT}');
        ws.onopen = () => console.log('WebSocket connection established.');
        ws.onmessage = event => {{
            console.log('Text received:', event.data);
            textElement.textContent = event.data;
        }};
        ws.onclose = () => {{
            console.log('WebSocket connection closed.');
            textElement.textContent = 'Connection lost. Please restart the Python server and refresh the page.';
        }};
    </script>
</body>
</html>
"""

async def text_update_handler(websocket):
    connected_clients.add(websocket)
    print("Browser connected.")
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)
        print("Browser disconnected.")

async def start_websocket_server():
    # THE FIX IS HERE: Added 'ping_interval=None' to prevent timeouts
    # while waiting for user input.
    async with websockets.serve(
        text_update_handler, "localhost", WEBSOCKET_PORT, ping_interval=None
    ):
        await asyncio.Future()  # run forever

def start_http_server():
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(html_content, "utf8"))
        # Suppress logging of GET requests to clean up terminal output
        def log_message(self, format, *args):
            return

    with socketserver.TCPServer(("", HTTP_PORT), CustomHandler) as httpd:
        print(f"HTTP server started at http://localhost:{HTTP_PORT}/")
        httpd.serve_forever()

async def main():
    print("Starting servers...")
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()

    websocket_server_task = asyncio.create_task(start_websocket_server())

    print("--- Ready to send text to your browser ---")
    while True:
        text_to_send = await asyncio.to_thread(input, "Enter text to read: ")
        
        if connected_clients:
            # A more robust way to send to all clients
            tasks = [client.send(text_to_send) for client in connected_clients]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Log any errors that might have occurred during sending
            for result in results:
                if isinstance(result, Exception):
                    print(f"Failed to send to a client (they may have disconnected): {result}")
            
            # Avoid printing if the input was empty
            if text_to_send:
                print(f"Sent: '{text_to_send}'")
        else:
            print("No browser connected. Please open/refresh the page.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    except Exception as e:
        print("\nAn unexpected error occurred:")
        traceback.print_exc()