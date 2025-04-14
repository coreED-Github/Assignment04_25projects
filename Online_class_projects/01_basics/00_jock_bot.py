import random

PROMPT = "What do you want? "
JOKES = [
    "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python programmer go hungry? Because his food was stuck in a tuple!",
    "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
    "What do you call 8 hobbits? A hobbyte."
]
SORRY = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT).strip()

    if user_input.lower() == "joke":
        joke = random.choice(JOKES)
        print(joke)
    else:
        print(SORRY)

if __name__ == '__main__':
    main()