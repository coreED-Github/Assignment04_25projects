import random

def main():
    print("=== Welcome to 'Guess My Secret Number' ===")
    print("I'm thinking of a number between 1 and 99...\n")

    play_again = "yes"
    
    while play_again.lower() in ["yes", "y"]:
        secret_number = random.randint(1, 99)
        attempts = 0
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
                
                if guess < secret_number:
                    print("Too low! Try again.\n")
                elif guess > secret_number:
                    print("Too high! Try again.\n")
                else:
                    print(f"Congrats! You guessed it in {attempts} tries. The number was: {secret_number}")
                    break
            except ValueError:
                print("Please enter a valid number.\n")
        
        play_again = input("\nWant to play again? (yes/no): ")
        print()

    print("Thanks for playing! Goodbye.")

if __name__ == '__main__':
    main()