def main():
    print("Welcome to the Number Booster!")
    try:
        curr_value = int(input("Enter a starting number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("\nBoosting your number...")

    while curr_value < 100:
        curr_value = curr_value * 2
        print(f"Boosted to: {curr_value}")

    print("\nCongrats! You've crossed 100. Final value:", curr_value)


if __name__ == '__main__':
    main()