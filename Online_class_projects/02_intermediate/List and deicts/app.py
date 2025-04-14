def main():

    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    print(f"Length of the list: {len(fruit_list)}")

    fruit_list.append('mango')

    print("Updated list:", fruit_list)

def access_element(my_list, index):
    if index < 0 or index >= len(my_list):
        return "Index out of range"
    return my_list[index]

def modify_element(my_list, index, new_value):
    if index < 0 or index >= len(my_list):
        return "Index out of range"
    my_list[index] = new_value
    return my_list

def slice_list(my_list, start, end):
    if start < 0 or end > len(my_list):
        return "Index out of range"
    return my_list[start:end]

def play_game():
    my_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    print("Welcome to the Index Game!")
    print("Your list:", my_list)
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print(f"Accessed Element: {result}")

        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print(f"Modified List: {result}")

        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(my_list, start, end)
            print(f"Sliced List: {result}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
    play_game()