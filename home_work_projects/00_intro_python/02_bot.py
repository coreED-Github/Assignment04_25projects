def main():
    print("Welcome to the Animal Lover Program!")
    animal = input("What's your favorite animal? ").strip().lower()

    formatted_animal = animal.capitalize()

    print(f"My favorite animal is also {formatted_animal}!")

if __name__ == '__main__':
    main()