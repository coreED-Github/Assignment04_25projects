def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("\033[91mInvalid input! Please enter a valid integer.\033[0m")

def add_numbers(a, b):
    return a + b

def display_result(result):
    print(f"\033[92mThe total sum is: {result}\033[0m")

def main():
    print("\033[96mWelcome to the Simple Adder Program!\033[0m")
    num1 = get_integer("Enter the first number: ")
    num2 = get_integer("Enter the second number: ")
    total = add_numbers(num1, num2)
    display_result(total)

if __name__ == '__main__':
    main()