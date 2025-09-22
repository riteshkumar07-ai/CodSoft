import random

# score
u_score = 0
c_score = 0
choices = ["rock", "paper", "scissor"]

# history list
history = []

# menu
def game_menu():
    print("\n----- Welcome to Rock-Paper-Scissor Game ------")
    print("1. Start Game")
    print("2. See History")
    print("3. Exit Game")

def start_game():
    global u_score, c_score, history   # use global variables
    
    your_choice = input("Choose rock, paper or scissor : ").lower()
    comp_choice = random.choice(choices)   # always define before
    
    if your_choice not in choices:
        print("Invalid choice! Try again.")
        return
    
    print("Computer chose : ", comp_choice)
    
    if your_choice == comp_choice:
        result = "Tie"
        print("It's a Tie\n")
    elif (your_choice == "rock" and comp_choice == "scissor") or \
         (your_choice == "scissor" and comp_choice == "paper") or \
         (your_choice == "paper" and comp_choice == "rock"):
        result = "You Win"
        print("You Win!\n")
        u_score += 1
    else:
        result = "Computer Win"
        print("Computer Wins!\n")
        c_score += 1

    # save to history
    history.append((your_choice, comp_choice, result))

    print("Score:")
    print("You : ", u_score, " | Computer : ", c_score)

def see_history():
    if not history:
        print("\nNo games played yet!")
    else:
        print("\n----- Game History -----")
        for i, (u, c, r) in enumerate(history, start=1):
            print(f"{i}. You: {u} | Computer: {c} | Result: {r}")
        print("------------------------")

# main loop
while True:
    game_menu()
    try:
        opt = int(input("Choose an option : "))
    except ValueError:
        print("Enter a valid number!")
        continue

    if opt == 1:
        start_game()
    elif opt == 2:
        see_history()
    elif opt == 3:
        print("Exiting game... Bye!")
        break
    else:
        print("Invalid option! Try again.")
