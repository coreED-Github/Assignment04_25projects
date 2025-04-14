ADULT_AGE = 18

def is_adult(age: int) -> bool:
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))
    if is_adult(age):
        print(f"Entered age is an adult age: {age} years old")
        print(True)
    else:
        print(f"Entered age is not an adult age: {age} years old")
        print(False)

if __name__ == '__main__':
    main()