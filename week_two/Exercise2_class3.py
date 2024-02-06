# problem
import time as t
periods = ['Morning', 'Afternoon', 'Evening']
for a in periods:
    print('Good ' + a, '\n','How are you feeling?')
    feeling = str(input())
    print ('I am happy to hear that you are feeling ' + feeling + '.')