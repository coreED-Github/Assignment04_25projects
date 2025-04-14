def average(*numbers: float):
    """
    Returns the average of all input numbers.
    Accepts any number of arguments.
    """
    if not numbers:
        return 0
    return round(sum(numbers) / len(numbers), 2)

def main():

    print("Average of 5 and 15:", average(5, 15))

    print("Average of 1, 2, 3, 4, 5:", average(1, 2, 3, 4, 5))

    print("Average with no input:", average())

    nums = [10, 20, 30, 40]
    print("Average of", nums, ":", average(*nums))

if __name__ == '__main__':
    main()