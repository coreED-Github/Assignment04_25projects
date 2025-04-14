def read_phone_numbers():
    """
    Reads names and phone numbers from user input and stores them in a dictionary.
    """
    phonebook = {}

    while True:
        name = input("Name (Leave empty to stop): ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Displays the full phonebook.
    """
    print("\n--- Phonebook ---")
    if not phonebook:
        print("Phonebook is empty.")
    else:
        for name, number in phonebook.items():
            print(f"{name} -> {number}")
    print("-----------------\n")

def lookup_by_name(phonebook):
    """
    Looks up a number using a contact name.
    """
    name = input("Enter name to lookup: ")
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}")
    else:
        print(f"{name} is not in the phonebook.")

def lookup_by_number(phonebook):
    """
    Finds and prints the name associated with a given number.
    """
    number = input("Enter number to lookup: ")
    found = False
    for name, num in phonebook.items():
        if num == number:
            print(f"The number {number} belongs to {name}")
            found = True
            break
    if not found:
        print(f"The number {number} is not in the phonebook.")

def delete_contact(phonebook):
    """
    Deletes a contact from the phonebook.
    """
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} has been deleted.")
    else:
        print(f"{name} was not found in the phonebook.")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)

    while True:
        print("Options: [1] Lookup by name, [2] Lookup by number, [3] Delete contact, [4] Show all, [Enter] to exit")
        choice = input("Choose an option: ")
        
        if choice == "":
            break
        elif choice == "1":
            lookup_by_name(phonebook)
        elif choice == "2":
            lookup_by_number(phonebook)
        elif choice == "3":
            delete_contact(phonebook)
        elif choice == "4":
            print_phonebook(phonebook)
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()