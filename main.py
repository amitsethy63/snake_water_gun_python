import random

def get_winner(user, computer):
    if (user == computer):
        return "draw"
    elif(user == "snake" and computer == "water") or \
        (user == "gun" and computer == "snake") or \
        (user == "water" and computer == "gun"):
        return "user"
    else:
        return "computer"
    
def snake_water_gun():
    choices = ["snake", "water", "gun"]
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose snake, water or gun : ").lower()

        if user_choice not in choices:
            print("Invalid choices! Try again.\n")
            continue

        computer_choice = random.choice(choices)

        print(f"User Choice : {user_choice}")
        print(f"Computer Choice : {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if(winner == "user"):
            print("You Win!")
            user_score += 1
        elif(winner == "computer"):
            print("Computer Wins!")
            computer_score += 1
        else:
            print("It's a draw.")

        print(f"Score -> You : {user_score} | Computer : {computer_score}")    

        play_again = input("Play Again(Yes/No): ").lower()

        if (play_again != "yes"):
            print("Thank you for playing.")
            break
        print()        

snake_water_gun()        

        
    

