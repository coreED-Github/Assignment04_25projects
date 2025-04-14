def count_even(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    print(f"\nYou entered {len(lst)} numbers.")
    print(f"Even numbers ({len(even_numbers)}): {even_numbers}")

def get_list_of_ints():
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        try:
            lst.append(int(user_input))
        except ValueError:
            print("That's not a valid integer. Try again.")
        user_input = input("Enter an integer or press enter to stop: ")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()