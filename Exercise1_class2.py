# 1. Write a program to prompt the user for hours and rate
# per hour to compute gross pay.

# Example:
# Enter Hours: 35
# Enter Rate: 2.75

# Result:
# Pay: 96.25

hours = input('How many hours you work?\n')
rate = input('Enter your rate:\n')
try:
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
        result = round(((hours-40)*(rate*1.5)+40*rate),2)
    else:
        result = round(hours*rate,2)

    print(format('Your salary is going to be:', result + '.2f'))
except ValueError:
    print('Value Incorrect')


