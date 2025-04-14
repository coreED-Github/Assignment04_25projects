import random

NUM_ROUNDS = 5

def play_high_low():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {your_number}")

        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        while guess not in ['higher', 'lower']:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        if (guess == 'higher' and your_number > computer_number) or (guess == 'lower' and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            if your_number == computer_number:
                print(f"Aww, that's incorrect. The computer's number was {computer_number}. It's a tie!")
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")

    print("Thanks for playing!")
    
    if score == NUM_ROUNDS:
        print(f"Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print(f"Good job, you played really well!")
    else:
        print(f"Better luck next time!")

play_high_low()