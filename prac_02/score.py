import random


def main():
    score = get_score()
    grade = different_grade(score)
    print(f"Score:{score}")
    print(f"Grade:{grade}")

    random_score = random.randint(0, 100)
    print(f"Random Grade:{random_score}")


def get_score():
    score = float(input("Enter score: "))
    return score


def different_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 50:
            return "Passable"
        elif score >= 90:
            return "Excellent"
        elif score < 50:
            return "Bad"


main()
