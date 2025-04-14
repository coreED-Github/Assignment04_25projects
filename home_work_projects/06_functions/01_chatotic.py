import random

MOODS = {
    "Energetic": 0.05,
    "Neutral": 0.25,
    "Lazy": 0.5,
    "Grumpy": 0.8
}

mood = random.choice(list(MOODS.keys()))
DONE_LIKELIHOOD = MOODS[mood]

def done():
    """Returns True with a probability of DONE_LIKELIHOOD."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    print(f"My mood today is: {mood} (I might stop early!)")
    for i in range(1, 11):
        if done():
            return
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()