def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")

    while True:
        try:
            part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
            if part_of_speech in [0, 1, 2]:
                break
            else:
                print("Invalid input! Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a valid number (0, 1, or 2).")

    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()