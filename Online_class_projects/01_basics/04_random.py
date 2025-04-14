import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print("=== Welcome to the Random Number Generator Challenge ===\n")
    
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)

        if num < 50:
            print(f"{num} - Low Range!")
        elif 50 <= num <= 75:
            print(f"{num} - Medium Range!")
        else:
            print(f"{num} - High Range!")

if __name__ == '__main__':
    main()