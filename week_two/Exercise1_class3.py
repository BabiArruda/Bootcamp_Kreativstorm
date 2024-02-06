# 1. Rewrite your pay computation with time-and-a-half for overtime and create a
# function called computepay which takes two parameters
# (hours and rate).

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(h, r):
    if h > 40:
        result = round(((h-40)*(r*1.5)+40*r),2)
    else:
        result = round(h*r,2)

    return result

try:
    hours = float(input('How many hours you work?\n'))
    rate = float(input('Enter your rate:\n'))

except ValueError:
    print('Value Incorrect')
    quit()

print(f'Your salary is going to be: {computepay(hours, rate)}')