# ============================================
# Challenge Set 10 Solutions
# ============================================

# --------------------------------------------
# Question 1 — Roll Until Six 🎲
# --------------------------------------------

import random

while True:
    roll = random.randint(1, 6)
    print("You rolled:", roll)

    if roll == 6:
        print("You won!")
        break


# --------------------------------------------
# Question 2 — Lucky Student 🎓
# --------------------------------------------

import random

students = [
    "Radhika",
    "Aman",
    "Priya",
    "Karan",
    "Rahul",
    "Neha"
]

print("\nThe three lucky winners are:")

winners = random.sample(students, 3)

for winner in winners:
    print(winner)


# --------------------------------------------
# Question 3 — Student Analytics 📊
# --------------------------------------------

import statistics

marks = [92, 78, 85, 95, 67, 88, 73]

highest = max(marks)
lowest = min(marks)
mean = statistics.mean(marks)
median = statistics.median(marks)
data_range = highest - lowest

print("\nHighest:", highest)
print("Lowest:", lowest)
print("Mean:", mean)
print("Median:", median)
print("Range:", data_range)


# --------------------------------------------
# Question 4 — Username Formatter
# --------------------------------------------

username = input("\nEnter a username: ")

print("First 5 characters:", username[:5])
print("Last 4 characters:", username[-4:])
print("Username length:", len(username))


# --------------------------------------------
# Question 5 — Random Password Generator 🔐
# --------------------------------------------

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

characters = letters + numbers

password = "".join(random.choices(characters, k=8))

print("\nGenerated Password:", password)


# --------------------------------------------
# Question 6 — Playlist Shuffle 🎵
# --------------------------------------------

import random

songs = [
    "Believer",
    "Perfect",
    "Skyfall",
    "Shape of You",
    "Bones"
]

random.shuffle(songs)

print("\nShuffled Playlist:")

for song in songs:
    print(song)


# --------------------------------------------
# Question 7 — Mini Statistics App
# --------------------------------------------

import statistics

count = int(input("\nHow many numbers do you want to enter? "))

numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("\nMean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Highest:", max(numbers))
print("Lowest:", min(numbers))


# --------------------------------------------
# Question 8 — Build Your Own Utility Library 📦
# --------------------------------------------

from math_utils import average, highest, lowest

numbers = [4, 6, 3, 2, 6, 7, 8, 9, 6, 4, 3, 24, 54, 6, 3]

print("\nAverage:", average(numbers))
print("Highest:", highest(numbers))
print("Lowest:", lowest(numbers))

# --------------------------------------------
# math_utils.py
# --------------------------------------------

def average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def highest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def lowest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

# --------------------------------------------
# Question 9 — String Slicing Challenge
# --------------------------------------------

sentence = "Python Programming"

print("\n", sentence[:6], sep="")
print(sentence[7:])
print(sentence[::2])
print(sentence[::-1])


# --------------------------------------------
# Question 10 — Number Lottery 🎰
# --------------------------------------------

import random

lottery_numbers = random.sample(range(1, 51), 6)

print("\nLottery Numbers:")

for number in lottery_numbers:
    print(number)


# --------------------------------------------
# ⭐ Bonus Project — Student Performance Analyzer
# --------------------------------------------

import statistics

students = {
    "Radhika": [90, 85, 88],
    "Aman": [70, 60, 80],
    "Priya": [95, 91, 97],
    "Karan": [50, 45, 55],
}


def calculate_average(marks):
    return statistics.mean(marks)


def calculate_highest(marks):
    return max(marks)


def calculate_lowest(marks):
    return min(marks)


def performance(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 75:
        return "Good"
    else:
        return "Needs Improvement"


for name, marks in students.items():
    avg = calculate_average(marks)

    print(f"\n{name}")
    print("-" * len(name))
    print("Average :", avg)
    print("Highest :", calculate_highest(marks))
    print("Lowest  :", calculate_lowest(marks))
    print("Remarks :", performance(avg))