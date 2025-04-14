import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    attempts = 0
    guess = int(input("Enter a guess: "))
    attempts += 1

    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()
        guess = int(input("Enter a new guess: "))
        attempts += 1

    print(f"Congrats! The number was: {secret_number}")
    print(f"You guessed it in {attempts} attempts.")

if __name__ == '__main__':
    main()