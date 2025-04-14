"""
Program: dice_simulator
------------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

import random

NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    #random numbers for both dice
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    #both dice
    total = die1 + die2
    
    #rolls and the total
    print(f"Roll: Die 1 = {die1}, Die 2 = {die2}, Total = {total}")

def main():
    die1 = 10
    print("Initial value of die1 in main():", die1)

    roll_dice()
    roll_dice()
    roll_dice()

    print("Final value of die1 in main():", die1)

if __name__ == '__main__':
    main()