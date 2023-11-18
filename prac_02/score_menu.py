"""
CP1404/CP5632 - Practical 2
Score menu
"""

import random


MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input("Choice:").upper()
    while choice != "Q":
        if choice == "G":
            score = random.randint(0, 100)
            print(score)
        elif choice == "P":
            import score
        elif choice == "S":
            score = random.randint(0, 100)
            print(score * "*")
        print(MENU)
        choice = input("Choice:").upper()
    else:
        print("Farewell.")


main()
