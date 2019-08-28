
sales = float(input("Enter the sales: $"))
if sales < 1000:
    bonus = sales * 0.10
else:
    bonus = sales * 0.15
print("The Bonus is: " + str(bonus))
