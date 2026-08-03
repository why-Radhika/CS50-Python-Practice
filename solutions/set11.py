"""
Set 11 - Functions, Dictionaries & Mini Projects

Note:
This set focuses on practicing functions, dictionaries, modules,
randomization, and mini projects from the lecture.
"""

# ============================================
# Question 1 — Student Dashboard 📊
# ============================================

import statistics

students = {
    "Radhika": [90, 88, 95],
    "Aman": [70, 82, 76],
    "Priya": [98, 96, 99],
    "Karan": [45, 60, 55]
}


def calculate_average(marks):
    return statistics.mean(marks)


def calculate_highest(marks):
    return max(marks)


def calculate_lowest(marks):
    return min(marks)


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"


for name, marks in students.items():
    avg = calculate_average(marks)
    high = calculate_highest(marks)
    low = calculate_lowest(marks)

    print(f"--- {name} ---")
    print("Average:", avg)
    print("Highest:", high)
    print("Lowest:", low)
    print("Grade:", grade(avg))
    print()


# ============================================
# Question 2 — Password Generator Pro 🔐
# ============================================

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

all_chars = letters + numbers

length = int(input("Enter the password length: "))

password = "".join(random.choices(all_chars, k=length))

print("Generated Password:", password)


# ============================================
# Question 3 — Guess the Celebrity 🎲
# ============================================

import random

celebrities = {
    "SRK": "Shah Rukh Khan",
    "MSD": "MS Dhoni",
    "VK": "Virat Kohli",
    "RDJ": "Robert Downey Jr."
}

question = random.choice(list(celebrities.keys()))

print("Who is", question + "?")

user_guess = input("Your answer: ")

if user_guess.lower() == celebrities[question].lower():
    print("Correct Answer!")
else:
    print("Wrong!")
    print("Correct Answer:", celebrities[question])


# ============================================
# Question 4 — Your Own Statistics Library 📦
# ============================================

from stats_utils import average, highest, lowest, grade

marks = [90, 78, 87, 86, 94]

avg = average(marks)
high = highest(marks)
low = lowest(marks)

print("Average:", avg)
print("Highest:", high)
print("Lowest:", low)
print("Grade:", grade(avg))


"""
stats_utils.py

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


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"
"""


# ============================================
# Question 5 — Mini Text Analyzer ✂️
# ============================================

sentence = input("Enter a sentence: ")

clean_sentence = sentence.strip()

all_char = len(sentence)
all_char_wo_space = len(sentence.replace(" ", ""))

words = clean_sentence.split()

word_count = len(words)

first_word = words[0] if words else ""
last_word = words[-1] if words else ""

reverse_words = " ".join(words[::-1])
reverse_chars = sentence[::-1]
second_char = sentence[1::2]

print(f"Total Characters (with spaces): {all_char}")
print(f"Total Characters (no spaces):   {all_char_wo_space}")
print(f"Total Words:                    {word_count}")
print(f"First Word:                     {first_word}")
print(f"Last Word:                      {last_word}")
print(f"Reverse Words:                  {reverse_words}")
print(f"Reverse Characters:             {reverse_chars}")
print(f"Every 2nd Character:            {second_char}")


# ============================================
# ⭐ Final Project — Classroom Manager
# ============================================

from school_utils import average, highest, lowest, class_average
import random

students = {
    "Radhika": [90, 80, 95],
    "Aman": [70, 82, 78],
    "Priya": [99, 95, 97]
}

while True:
    action = int(input(
        "\nChoose what to do:\n"
        "1 - View Student\n"
        "2 - View Class Average\n"
        "3 - Pick Random Student\n"
        "4 - Exit\n"
        "Choice: "
    ))

    if action == 1:
        name = input("Enter the student name: ").strip().title()

        if name in students:
            marks = students[name]

            print("Marks:", marks)
            print("Average:", average(marks))
            print("Highest Marks:", highest(marks))
            print("Lowest Marks:", lowest(marks))
        else:
            print("Student not found!")
            continue

    elif action == 2:
        print("Class Average:", class_average(students))

    elif action == 3:
        name = random.choice(list(students.keys()))
        marks = students[name]

        print("Random Student:", name)
        print("Marks:", marks)
        print("Average:", average(marks))
        print("Highest Marks:", highest(marks))
        print("Lowest Marks:", lowest(marks))

    elif action == 4:
        print("Thanks!")
        break

    else:
        print("Invalid choice.")


"""
school_utils.py

def average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)


def highest(marks):
    largest = marks[0]

    for number in marks:
        if number > largest:
            largest = number

    return largest


def lowest(marks):
    smallest = marks[0]

    for number in marks:
        if number < smallest:
            smallest = number

    return smallest


def class_average(students):
    student_averages = [average(marks) for marks in students.values()]
    return average(student_averages)
"""