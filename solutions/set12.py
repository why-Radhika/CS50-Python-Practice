"""
===========================================
Set 12 — Unit Testing Fundamentals
===========================================

Each question should have:
1. A Python file (example: square.py)
2. A pytest file (example: test_square.py)

This file contains only the solution functions.
"""

# ==========================================
# Question 1 — Square Function
# ==========================================

def main():

    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    square = n * n
    return square

if __name__ == "__main__":
    main()


# test_calculator.py

from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(5) == 25

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-5) == 25

def test_zero():
    assert square(0) == 0


# ==========================================
# Question 2 — Even Number Checker
# ==========================================

def main():

    x = int(input("What's x? "))
    if is_even(x):
        print("Yes it is even")
    else:
        print("No it is odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()


# test_even.py

from even import is_even

def test_positive():
    assert is_even(2) is True
    assert is_even(7) is False

def test_negative():
    assert is_even(-4) is True

def test_zero():
    assert is_even(0) is True


# ==========================================
# Question 3 — Grade Calculator
# ==========================================

def main():
    marks = int(input("Enter your marks: "))
    print("Your grade is", grade(marks))

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

if __name__ == "__main__":
    main()


# test_grades.py

from grades import grade

def test_grades():
    assert grade(95) == "A"
    assert grade(90) == "A"
    assert grade(89) == "B"
    assert grade(80) == "B"
    assert grade(70) == "C"
    assert grade(45) == "D"


# ==========================================
# Question 4 — Username Formatter
# ==========================================

def main():
    name = input("Enter your name: ")
    print(format_username(name))

def format_username(name):
    name = name.strip().title()
    if name == "":
        return "Invalid Input"
    else:
        return name

if __name__ == "__main__":
    main()


# test_username.py

from username import format_username

def test_default():
    assert format_username("Radhika    ") == "Radhika"
    assert format_username("Radhika") == "Radhika"

def test_allup():
    assert format_username("RADHIKA  ") == "Radhika"

def test_empty():
    assert format_username("") == "Invalid Input"


# ==========================================
# Question 5 — Reverse String
# ==========================================

def main():
    text = input("Enter your name: ")
    print(reverse(text))

def reverse(text):
    rev_text = text[::-1]
    return rev_text

if __name__ == "__main__":
    main()


# test_reverse.py

from reverse import reverse

def test_default():
    assert reverse("Python") == "nohtyP"
    assert reverse("Python is cool") == "looc si nohtyP"

def test_special():
    assert reverse("P") == "P"
    assert reverse("Kayak") == "kayaK"

def test_empty():
    assert reverse("") == ""


# ==========================================
# Question 6 — Count Vowels
# ==========================================

def main():
    text = input("Enter a word/sentence: ")
    print(count_vowels(text))

def count_vowels(text):
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    main()


# test_vowels.py

from vowels import count_vowels

def test_default():
    assert count_vowels("rtyws") == 0
    assert count_vowels("Natural") == 3

def test_special():
    assert count_vowels("APPLE") == 2

def test_empty():
    assert count_vowels("") == 0


# ==========================================
# Question 7 — Average Calculator
# ==========================================

def main():
    nums = []
    length = int(input("Enter the length of the list: "))

    for i in range(length):
        nums.append(int(input(f"Enter number {i + 1}: ")))

    print("The average is", average(nums, length))

def average(numbers, length):
    total = 0

    if length == 0:
        return "Invalid"

    for number in numbers:
        total += number
        avg = total / length

    return avg

if __name__ == "__main__":
    main()


# test_average.py

from average import average

def test_default():
    assert average([1,2,3],3) == 2
    assert average([10],1) == 10
    assert average([5,5,5],3) == 5

def test_empty():
    assert average([],0) == "Invalid"


# ==========================================
# Question 8 — Password Validator
# ==========================================

def main():
    password = input("Enter a password: ")

    if valid_password(password):
        print("Your password is strong")
    else:
        print("Your password is not strong")

def valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

if __name__ == "__main__":
    main()


# test_password.py

from password import valid_password

def test_default():
    assert valid_password("vdhfvher") is True
    assert valid_password("1234567") is False
    assert valid_password("vhuqfu399u2rhufbi2903h") is True

def test_empty():
    assert valid_password("") is False


# ==========================================
# ⭐ Bonus Challenge — Test First
# ==========================================

def main():
    text = input("Enter something: ")

    if is_palindrome(text):
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")

def is_palindrome(text):
    text = text.lower()
    reverse = text[::-1]

    if text == reverse:
        return True
    else:
        return False

if __name__ == "__main__":
    main()


# test_palindrome.py

from palindrome import is_palindrome

def test_default():
    assert is_palindrome("Kayak") is True
    assert is_palindrome("Alert") is False

def test_numbers():
    assert is_palindrome("111") is True
    assert is_palindrome("124") is False

def test_empty():
    assert is_palindrome("") is True
    assert is_palindrome("  ") is True