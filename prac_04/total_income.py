"""
CP1404/CP5632 Practical - Suggested Solution
Cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes_per_month = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(
            input("Enter income for month {}: ".format(month)))
        incomes_per_month.append(income)

    print_report(incomes_per_month)


def print_report(incomes_per_month):
    """Print report based on incomes."""
    # Note that we do not need to pass in number_of_months
    # because we know the length of the incomes list
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes_per_month):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))


main()
