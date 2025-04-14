MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0
    next_term = 1
    index = 0

    while curr_term <= MAX_TERM_VALUE:
        print(f"Fib({index}) = {curr_term}")
        curr_term, next_term = next_term, curr_term + next_term
        index += 1

if __name__ == '__main__':
    main()

