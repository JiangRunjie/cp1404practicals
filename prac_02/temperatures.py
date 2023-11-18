"""
CP1404/CP5632 - Practical 2
Temperatures
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit(float(input("Celsius: ")))
        elif choice == "F":
            fahrenheit_to_celsius(float(input("Fahrenheit: ")))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()
