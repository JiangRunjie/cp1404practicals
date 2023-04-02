# 1.
out_file = open('name.txt', 'w')
name = input("Enter your name:")
print(f"{name}", file=out_file)
out_file.close()

# 2.
out_file = open('name.txt', 'r')
name = out_file.readline()
print(f"Your name is {name}.")
out_file.close()

# 3.
out_file = open('numbers.txt', 'r')
number = out_file.readlines() + out_file.readlines()
total = int(number[0].rstrip("\n")) + int(number[1].rstrip("\n"))
print(total)
out_file.close()

# 4.
out_file = open('numbers.txt', 'r')
total = 0
for line in out_file:
    number = int(line)
    total += number
print(total)
out_file.close()
