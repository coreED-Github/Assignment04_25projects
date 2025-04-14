AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation:\n" + AFFIRMATION)

    user_input = input() 

    while user_input != AFFIRMATION:
        print("\nHmmm...")
        print("That was not the affirmation.")
        print("\nPlease type the following affirmation:\n" + AFFIRMATION)
        user_input = input()

    print("\nThat's right! :)")

if __name__ ==' __main__':
    main()