def main():
    voting_ages = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }
    
    try:
        user_age = int(input("How old are you? "))
        
        if user_age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            return

        for country, voting_age in voting_ages.items():
            if user_age >= voting_age:
                print(f"You can vote in {country} where the voting age is {voting_age}.")
            else:
                print(f"You cannot vote in {country} where the voting age is {voting_age}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")

if __name__ == '__main__':
    main()