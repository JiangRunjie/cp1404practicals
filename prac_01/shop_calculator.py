TOTAL_PRICE = 0
DISCOUNT = 0.1

items_number = int(input("Number of items: "))

while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Number of items: "))

for i in range(items_number):
    item_price = float(input("Number of items: "))
    TOTAL_PRICE += item_price

if TOTAL_PRICE > 100:
    TOTAL_PRICE *= (1 - DISCOUNT)

print("Total price for {0} items is ${1:.2f}".format(items_number, TOTAL_PRICE))

