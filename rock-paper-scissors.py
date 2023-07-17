import random
#The program will compare  choices between playaer and computer  to determine the winner based on the following rules:
#Rock beats scissors.
#Scissors beats paper.
#Paper beats rock.
#If both players choose the same option, it\'s a tie.
#the player plays multiple rounds and the program keeps track of the score until one player reaches a predetermined number of wins or until the player decide to stop..

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    if (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    return "Computer wins!"

while True:
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer chooses: {computer_choice}")

    if player_choice in choices:
        winner = determine_winner(player_choice, computer_choice)
        if winner == "You win!":
            player_score += 1
        elif winner == "Computer wins!":
            computer_score += 1
        print(winner)
    else:
        print("Invalid choice. Please try again.")

    print(f"Player Score: {player_score} | Computer Score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Game over!")