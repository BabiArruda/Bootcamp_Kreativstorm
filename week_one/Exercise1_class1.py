# 1. Write a program to prompt the user for hours and rate
# per hour to compute gross pay.

# Example:
# Enter Hours: 35
# Enter Rate: 2.75

# Result:
# Pay: 96.25

hours = float(input("How many hours you work?\n"))
rate = float(input("Enter your rate:\n"))
print(format("Your salary is going to be: ", hours * rate, ".2f"))
