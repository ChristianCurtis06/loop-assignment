# Task 1: Your Mood Tracker

# Imports 'random' module
import random

# Lists days of the week, times of day, and moods
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times_of_day = ['morning', 'afternoon', 'evening']
moods = ['sad', 'bored', 'tired', 'energetic', 'happy', 'elated']

# Iterates over list of days
for day in days:
    # Iterates over list of times of day and prints a random mood for each day and time
    for time in times_of_day:
        print(f"On {day} {time}, you were {random.choice(moods)}!")