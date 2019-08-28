
total = 0
number_of_items = int(input("Enter the  Number of items: "))
while number_of_items < 0:
    print("Invalid number")
    number_of_items = int(input("Enter the  Number of items: "))
for i in range(number_of_items):
    price = float(input("Enter the price of item " + str(i+1) + " "))
    total += price

if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(number_of_items, total))
