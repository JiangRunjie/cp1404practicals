# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number_of_star = int(input("Number of stars:"))
while number_of_star < 0:
    print("Invalid number.")
    number_of_star = int(input("Number of stars:"))
else:
    for i in range(number_of_star):
        print("*", end="")
print()

# d.
number_of_star = int(input("Number of stars:"))
for i in range(number_of_star):
    print((i + 1) * "*")
