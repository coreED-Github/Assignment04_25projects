import time
import datetime
import csv
import random
import sys
from IPython.display import Audio, display

alarm_sound_url = "https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg"

quotes = [
    "Keep going, you're doing great!",
    "Break done, now back to hustle!",
    "Progress is progress, no matter how small.",
    "Every step takes you closer to your goal!",
    "Hard work always pays off!"
]

purpose = input("What is the purpose of the timer? (Study, Cooking, Exercise, etc.): ")

print("\nChoose time unit:")
print("1. Seconds")
print("2. Minutes")
print("3. Hours")
unit_choice = input("Enter 1, 2 or 3: ")

while unit_choice not in ['1', '2', '3']:
    unit_choice = input("Invalid input. Please enter 1 for Seconds, 2 for Minutes, or 3 for Hours: ")

time_value = int(input("Enter the amount of time: "))

if unit_choice == '1':
    total_seconds = time_value
elif unit_choice == '2':
    total_seconds = time_value * 60
else:
    total_seconds = time_value * 3600

start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(seconds=total_seconds)

original_seconds = total_seconds

print(f"\033[1;36mPurpose:\033[0m {purpose}")
print(f"\033[1;35mEnds at:\033[0m {end_time.strftime('%I:%M:%S %p')}\n")

while total_seconds > 0:
    mins = total_seconds // 60
    secs = total_seconds % 60
    timer_display = f"{mins:02d}:{secs:02d}"

    bar_length = 30
    progress = int((original_seconds - total_seconds) / original_seconds * bar_length)
    bar = "[" + "#" * progress + "-" * (bar_length - progress) + "]"

    sys.stdout.write(f"\r\033[1;33mTime Remaining:\033[0m {timer_display} {bar}")
    sys.stdout.flush()

    time.sleep(1)
    total_seconds -= 1

print("\n")
print(f"\033[1;32m*** {purpose} time is up! ***\033[0m")
print("⏰ Alarm has gone off!")
print(f"\n\033[1;34mMotivational Quote:\033[0m {random.choice(quotes)}")

display(Audio(alarm_sound_url, autoplay=True))

log_entry = [datetime.datetime.now().isoformat(), purpose, f"{time_value} {'seconds' if unit_choice == '1' else 'minutes' if unit_choice == '2' else 'hours'}"]

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
            print(f"{row[0]} - {row[1]} ({row[2]})")
            total_sessions += 1
except FileNotFoundError:
    print("No previous log found.")

print(f"\n\033[1;32mTotal Sessions:\033[0m {total_sessions}")
