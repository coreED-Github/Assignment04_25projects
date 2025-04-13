# -*- coding: utf-8 -*-
"""copy-of-countdown-timer_06.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/coreED-Github/747039922ea5e4e062b3e52901fe56f9/copy-of-countdown-timer_06.ipynb
"""

import time
import datetime
import csv
import random
from IPython.display import clear_output, Audio, display

alarm_sound_url = "https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg"

quotes = [
    "Keep going, you’re doing great!",
    "Break done, now back to hustle!",
    "Progress is progress, no matter how small.",
    "Every step takes you closer to your goal!",
    "Hard work always pays off!"
]

purpose = input("What is the purpose of the timer? (Study, Cooking, Exercise, etc.): ")
minutes = int(input("How many minutes for the countdown? "))

total_seconds = minutes * 60
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(seconds=total_seconds)

original_seconds = total_seconds
while total_seconds > 0:
    mins = total_seconds // 60
    secs = total_seconds % 60
    timer_display = f"{mins:02d}:{secs:02d}"

    bar_length = 30
    progress = int((original_seconds - total_seconds) / original_seconds * bar_length)
    bar = "[" + "#" * progress + "-" * (bar_length - progress) + "]"

    clear_output(wait=True)
    print(f"\033[1;36mPurpose:\033[0m {purpose}")
    print(f"\033[1;33mTime Remaining:\033[0m {timer_display} {bar}")
    print(f"\033[1;35mEnds at:\033[0m {end_time.strftime('%I:%M:%S %p')}")

    time.sleep(1)
    total_seconds -= 1

clear_output()
print(f"\033[1;32m*** {purpose} time is up! ***\033[0m")
print("⏰ Alarm has gone off!")
print(f"\n\033[1;34mMotivational Quote:\033[0m {random.choice(quotes)}")

display(Audio(alarm_sound_url, autoplay=True))

log_entry = [datetime.datetime.now().isoformat(), purpose, minutes]

with open("timer_log.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(log_entry)

print("\n\033[1;36mRecent Timer Log:\033[0m")
total_sessions = 0
total_minutes = 0

try:
    with open("timer_log.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} - {row[1]} ({row[2]} mins)")
            total_sessions += 1
            total_minutes += int(row[2])
except FileNotFoundError:
    print("No previous log found.")

print(f"\n\033[1;32mTotal Sessions:\033[0m {total_sessions}")
print(f"\033[1;32mTotal Time Spent:\033[0m {total_minutes} minutes")