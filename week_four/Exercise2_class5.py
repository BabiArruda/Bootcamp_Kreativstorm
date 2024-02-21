#1. Write a lambda function that you can use as the key argument in the sorted() function
#to sort the list of tuples based on the ages in ascending (from low to high) order. After sorting,
#print the sorted list.

#2. You are given a list of numbers. Your task is to write Python code that calculates the average of these numbers using the reduce() function from the functools module and a lambda function.

#numbers = [10, 20, 30, 40, 50]

people = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("David", 35)]
print(lambda age: age.sort(), people)