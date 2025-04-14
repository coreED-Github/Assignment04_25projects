def get_user_numbers():
    """
    Collect numbers from the user until a blank input is given.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return user_numbers

def classify_and_count(nums):
    """
    Classify numbers as even or odd and count their occurrences.
    """
    even_counts = {}
    odd_counts = {}
    
    for num in nums:
        if num % 2 == 0:
            even_counts[num] = even_counts.get(num, 0) + 1
        else:
            odd_counts[num] = odd_counts.get(num, 0) + 1
    
    return even_counts, odd_counts

def print_results(even_counts, odd_counts):
    print("\nEven Numbers:")
    if even_counts:
        for num, count in even_counts.items():
            print(f"{num} appears {count} times.")
    else:
        print("No even numbers entered.")

    print("\nOdd Numbers:")
    if odd_counts:
        for num, count in odd_counts.items():
            print(f"{num} appears {count} times.")
    else:
        print("No odd numbers entered.")

def main():
    print("** Even/Odd Number Counter **")
    numbers = get_user_numbers()
    even_counts, odd_counts = classify_and_count(numbers)
    print_results(even_counts, odd_counts)

if __name__ == '__main__':
    main()