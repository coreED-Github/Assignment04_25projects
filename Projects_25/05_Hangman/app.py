# -*- coding: utf-8 -*-
"""another-copy-of-hangman_project_05.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/coreED-Github/e2addeb771f147246818dbb122d24570/another-copy-of-hangman_project_05.ipynb
"""

import random
import time

categories = {
    'Animals': ['elephant', 'tiger', 'kangaroo'],
    'Fruits': ['apple', 'banana', 'cherry'],
    'Countries': ['india', 'france', 'brazil'],
    'Movies': ['inception', 'gladiator', 'matrix']
}

hangman_images = [
    '''
      ------
      |    |
           |
           |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
           |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
      |    |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
     /|    |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
           |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
     /     |
           |
     =======
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
     =======
    '''
]
def give_hint(word):
    return f"The word starts with: {word[0]}"

def get_valid_input(guessed_letters, incorrect_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
        elif guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter!")
        else:
            return guess
def set_difficulty():
    while True:
        difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
        if difficulty == 'easy':
            return 8
        elif difficulty == 'medium':
            return 6
        elif difficulty == 'hard':
            return 4
        else:
            print("Invalid choice. Please choose again.")

def hangman_game():
    print("Choose a category:")
    for category in categories:
        print(category)
    category = input("Enter category: ").capitalize()

    word = random.choice(categories.get(category, []))
    if not word:
        print(f"No words found for category {category}. Try again.")
        return

    word_length = len(word)
    guesses_left = set_difficulty()
    guessed_letters = []
    incorrect_guesses = []
    display = ['_'] * word_length

    start_time = time.time()
    time_limit = 30
    hint_used = False

    if not hint_used:
        if input("Want a hint? (yes/no): ").lower() == "yes":
            print(give_hint(word))
            hint_used = True

    while guesses_left > 0 and '_' in display:
        print(f"\nWord: {' '.join(display)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Guesses left: {guesses_left}")
        print(f"Time left: {max(0, time_limit - int(time.time() - start_time))} seconds")

        if time.time() - start_time > time_limit:
            print("Time's up! You lose.")
            break

        print(hangman_images[len(incorrect_guesses)])

        guess = get_valid_input(guessed_letters, incorrect_guesses)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            guessed_letters.append(guess)
            display = [guess if word[i] == guess else display[i] for i in range(word_length)]
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            incorrect_guesses.append(guess)
            guesses_left -= 1

    if '_' not in display:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Game Over! The word was: {word}")

def play_hangman():
    total_games = 0
    games_won = 0
    high_score = float('inf')

    while True:
        print("\nStarting a new game...")
        hangman_game()

        # total_games += 1
        # if '_' not in display:
        #     games_won += 1
        #     high_score = min(high_score, guesses_left)

        print(f"\nTotal Games Played: {total_games}")
        print(f"Games Won: {games_won}")
        print(f"High Score (Fewest guesses left): {high_score}")

        if input("\nDo you want to play again? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    play_hangman()