# Task 1: Your Mood Today

# Imports 'random' module
import random

# Lists days of the week and moods
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
moods = ['sad', 'bored', 'tired', 'energetic', 'happy', 'elated']

# Iterates over list of days using the 'range()' function and prints a random mood for each day
for i in range(7):
    print(f"On {days[i]}, you were {random.choice(moods)}!")