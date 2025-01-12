#User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) forthe computer.
#Game Logic: Determine the winner based on the user's choice and the
#computer's choice.
#Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice.
#Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores for
#multiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions and
#feedback.
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock, Paper, Scissors ---")
        user_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()

        if user_choice == "quit":
            print("\nThank you for playing!")
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, result)
        print(f"Scores - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
