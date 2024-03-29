'''
write a function named greet(func)

inside greet(func) create another function that does the following:
	1. print something
	2. a variable that uses func to access different arguments (*args)

define another function called say_hello() which prints something
and by calling say_hello() at the end, also the greet(func) should be
provoked.

'''

def greet():
    def print_greet():
        print('Hello World')