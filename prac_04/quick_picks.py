import random

MINIMUM = 1
MAXIMUM = 45
LENGTH_OF_QUICK_PICK = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    quick_picks = []
    for i in range(number_of_quick_picks):
        quick_pick = generate_a_quick_pick()
        quick_picks.append(quick_pick)

    for quick_pick in quick_picks:
        format_print_quick_pick(quick_pick)


def test():
    quick_pick = generate_a_quick_pick()
    print(quick_pick)
    format_print_quick_pick(quick_pick)


def generate_a_quick_pick():
    numbers = []
    while len(numbers) < LENGTH_OF_QUICK_PICK:
        number = random.randint(MINIMUM, MAXIMUM + 1)
        if number not in numbers:
            numbers.append(number)

    return sorted(numbers)


def format_print_quick_pick(quick_pick):
    for number in quick_pick:
        print(f"{number:2d}", end=" ")
    print()


main()
