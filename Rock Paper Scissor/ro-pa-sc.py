#choice
import random
score = {"You": 0, "Computer": 0}
choices = ["rock","paper","scissor"]

#score
u_score = 0
c_score = 0

#menu
def game_menu():
    print("\n----- Welcome to Rock-Paper-Scissor Game ------")
    print("1. Start Game")
    print("2. See History")
    print("3. Exit Game")

def start_game():
    
    your_choice = input("Choose rock, paper or scissor : ").lower()
    if your_choice not in choices:
        print("Invalid choice! Try again.")
        comp_choice = random.choice(choices)
        print("Computer choose : ",comp_choice)
    elif (your_choice==comp_choice) :
        print("Its a Tie\n")
    elif (your_choice=="rock" and comp_choice=="scissor") or \
        (your_choice=="scissor" and comp_choice=="paper") or \
        (your_choice=="paper" and comp_choice=="rock"):
        print("You Win!\n")
    else :
        print("Computer Win!\n")
        c_score = c_score+1

    print("Score:")
    print("You : ",u_score," | Computer : ",c_score)
    

while True:
    game_menu()
    opt = int(input("Choose a option : "))
    if (opt==1):
        start_game()
