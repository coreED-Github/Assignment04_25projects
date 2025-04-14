import random
import time
from datetime import datetime

moves = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂"
}

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def get_user_choice():
    while True:
        choice = input("Choose Rock, Paper or Scissors: ").lower()
        if choice in moves:
            return choice
        else:
            print("Invalid input. Try again with 'rock', 'paper', or 'scissors'.")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    rounds = input("How many rounds do you want to play (odd number preferred)? ")

    while not rounds.isdigit() or int(rounds) <= 0:
        rounds = input("Please enter a valid positive number for rounds: ")

    rounds = int(rounds)
    player_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num} of {rounds}")
        player_choice = get_user_choice()
        computer_choice = random.choice(list(moves.keys()))
        
        print(f"You chose: {moves[player_choice]} ({player_choice})")
        print(f"Computer chose: {moves[computer_choice]} ({computer_choice})")

        result = get_winner(player_choice, computer_choice)

        if result == "player":
            print("You win this round!")
            player_score += 1
        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie this round!")

        print(f"Score => You: {player_score} | Computer: {computer_score}")
        time.sleep(1)

    print("\n--- Final Result ---")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > player_score:
        print("Sorry! The computer won this time.")
    else:
        print("It's a tie overall!")

    print(f"Final Score => You: {player_score} | Computer: {computer_score}")
    print("Game ended at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay in ["yes", "y"]:
        play_game()
    else:
        print("Thanks for playing!")

play_game()