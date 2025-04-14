def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0

    for fruit in fruits:
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * fruits[fruit]

    print(f"Your total is ${total_cost}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()