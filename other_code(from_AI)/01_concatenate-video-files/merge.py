from moviepy.editor import VideoFileClip, concatenate_videoclips

clips = [VideoFileClip(f"clip{i}.mp4") for i in range(1, 4)] # 3 videos

final = concatenate_videoclips(clips)
final.write_videofile("output.mp4", codec="libx264")
