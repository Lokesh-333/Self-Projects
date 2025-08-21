'''Hand Cricket'''
import random

# user defined function 1
def player_win_bat_computer_win_ball():
    print(f"{" "*25}| Player run/ball | Computer choice |")
    # ball one by computer
    computer_choice = random.choice(run_per_ball_list)
    player_choice = int(input("Enter ur run: "))
    player_runs = 0 # runs calculator variable
    if(player_choice == computer_choice):
        print(f"{" "*25}{player_choice} | {computer_choice} |")
        print("player is Duck out!")
        print(f"Total runs by player: {player_runs}")
    
    while(computer_choice != player_choice):
        player_runs = player_runs + player_choice
        print(f"{" "*25}| {player_choice} | {computer_choice} |")
        print(f"Total runs by player: {player_runs}")
        computer_choice = random.choice(run_per_ball_list)
        player_choice = int(input("Enter ur run: "))
        if(player_choice == computer_choice):
            print(f"{" "*25}| {player_choice} | {computer_choice} |")
            print("player is out!")
            print(f"Total runs by player: {player_runs}")
            break

    # now its computer turn to bat.
    print("now computer turn to bat, player balls")
    print(f"{" "*25}| player ball | Computer run/ball | Target : {player_runs} |")
    # ball one by player
    computer_choice = random.choice(run_per_ball_list)
    player_choice = int(input("Enter ur ball: "))
    computer_runs = 0 # runs calculator variable
    if(computer_choice == player_choice):
        print(f"{" "*25}| {player_choice} | {computer_choice} |")
        print("computer is Duck out!")
        print(f"player won by {player_runs - computer_runs} runs.")
    elif(computer_runs>player_runs):
            print(f"Computer won by {computer_runs - player_runs} runs.")
    else:
        while(computer_choice != player_choice):
            computer_runs = computer_runs + computer_choice
            if(computer_runs>player_runs):
                print(f"Computer won by {computer_runs - player_runs} runs.")
                break
            print(f"{" "*25}| {player_choice} | {computer_choice} |")
            print(f"{" "*25}Total runs by computer: {computer_runs}")
            computer_choice = random.choice(run_per_ball_list)
            player_choice = int(input("Enter ur run: "))
            if(computer_choice == player_choice):
                print(f"{" "*25}| {player_choice} | {computer_choice} |")
                print("computer is out!")
                print(f"player won by {player_runs - computer_runs} runs.")
                break

# userdefined function 2
def player_win_ball_computer_win_bat():
    print(f"{" "*25}| Player choise | Computer run/per |")
    # ball one by player
    computer_choice = random.choice(run_per_ball_list)
    player_choice = int(input("Enter ur ball: "))
    computer_runs = 0
    if(player_choice == computer_choice):
        print(f"{" "*25}{player_choice} | {computer_choice} |")
        print("computer is Duck out!")
        print(f"Total runs by computer: {computer_runs}")
    
    while(computer_choice != player_choice):
        computer_runs = computer_runs + computer_choice
        print(f"{" "*25}| {player_choice} | {computer_choice} |")
        print(f"Total runs by computer: {computer_runs}")
        computer_choice = random.choice(run_per_ball_list)
        player_choice = int(input("Enter ur ball: "))
        if(player_choice == computer_choice):
            print(f"{" "*25}| {player_choice} | {computer_choice} |")
            print("computer is out!")
            print(f"Total runs by computer: {computer_runs}")
            break

    # now its players turn to bat.
    print("now its players turn to bat, computer balls")
    print(f"{" "*25}| player ball | Computer run/ball | Target : {computer_runs} |")
    # ball one by computer
    computer_choice = random.choice(run_per_ball_list)
    player_choice = int(input("Enter ur ball: "))
    player_runs = 0
    if(computer_choice == player_choice):
        print(f"{" "*25}| {player_choice} | {computer_choice} |")
        print("player is Duck out!")
        print(f"computer won by {computer_runs} runs.")
    elif(player_runs>computer_runs): # if computer score is 0
            print(f"player won by {player_runs-computer_runs} runs.")
    else:
        while(computer_choice != player_choice):
            player_runs = player_runs + player_choice
            if(player_runs>computer_runs):
                print(f"player won by {player_runs - computer_runs} runs.")
                break
            print(f"{" "*25}| {player_choice} | {computer_choice} |")
            print(f"{" "*25}Total runs by player: {player_runs}")
            computer_choice = random.choice(run_per_ball_list)
            player_choice = int(input("Enter ur run: "))
            if(computer_choice == player_choice):
                print(f"{" "*25}| {player_choice} | {computer_choice} |")
                print("player is out!")
                print(f"computer won by {computer_runs - player_runs} runs.")
                break

# main function starts...

# to decide the all type of runs that can be made per ball
run_per_ball_list = []
max_runs = int(input("what should be max runs per ball: "))
for i in range(max_runs):
    run_per_ball_list.append(i+1)
'''computer asks player odd or even,
  if player choose even,the player has to choose a number ,
  if the sum of player toss and computer toss
  is even, then player wins the toss else computer will win the toss'''

odd_eve = input("Odd or Eve? (o or e): ")

computer_toss = random.choice([1, 2, 3, 4])
player_toss = int(input("Choose a number between 1-4: "))
sum_toss = player_toss + computer_toss
print(f"player : {player_toss}, computer : {computer_toss}, sum : {sum_toss}")

# player wins toss 
if((sum_toss%2==0 and odd_eve=="e") or (sum_toss%2!=0 and odd_eve=="o")):
    print("You won the toss!")
    toss_win = input("\nchoose to bat or ball: ")
    
    # if player chooses to bat as of winning the toss
    if (toss_win == "bat"):
        print("player chooses to bat.")
        player_win_bat_computer_win_ball()

    # if player chooses to ball as of winning the toss
    if(toss_win=="ball"):
        print("player chooses to ball.")
        player_win_ball_computer_win_bat()

# computer wins toss
if((sum_toss%2!=0 and odd_eve=="e") or (sum_toss%2==0 and odd_eve=="o")):
    print("computer won the toss!")
    toss_win = random.choice(["bat", "ball"])
    
    # if computer chooses to bat as of winning the toss
    if (toss_win == "bat"):
        print("computer chooses to bat.")
        player_win_ball_computer_win_bat()

    # if computer chooses to ball as of winning the toss
    if(toss_win=="ball"):
        print("computer chooses to ball.")
        player_win_bat_computer_win_ball()
            
print("Thanks player! for playing the game.")
