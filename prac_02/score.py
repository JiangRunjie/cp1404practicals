"""
CP1404/CP5632 - Practical 2
Score
"""

import random

HIGHEST_MARK = 100
LOWEST_MARK = 0


def main():
    score = check_input()
    grade = classify_grade(score)
    print(f"Score:{score}")
    print(f"Grade:{grade}")

    random_score = randomly_number()
    print(f"Random Grade:{random_score}")


def check_input():
    score = float(input("Enter score: "))
    while score < LOWEST_MARK or score > HIGHEST_MARK:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def classify_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


def randomly_number():
    return random.randint(LOWEST_MARK, HIGHEST_MARK)


main()
