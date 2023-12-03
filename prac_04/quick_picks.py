import random

MINI_NUM = 1
MAX_NUM = 45
LENGTH_OF_QUICK_PICK = 6

quick_pick = int(input("How many quick picks?"))

for i in range(quick_pick):
    numbers = []
    for j in range(LENGTH_OF_QUICK_PICK):
        random_number = random.randint(MINI_NUM, MAX_NUM)
        while random_number in numbers:
            random_number = random.randint(MINI_NUM, MAX_NUM)
        numbers.append(random_number)
        numbers.sort()
    for number in range(LENGTH_OF_QUICK_PICK):
        print(f"{numbers[number]:>2}", end=" ")
    print()
