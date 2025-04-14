def main():
    MINIMUM_HEIGHT = 50  # arbitrary units :)

    while True:
        user_input = input("How tall are you? ")
        
        if user_input == "":
            print("Goodbye! Come back next time!")
            break

        try:
            height = float(user_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        
        except ValueError:
            print("Please enter a valid number for your height.")

if __name__ == '__main__':
    main()