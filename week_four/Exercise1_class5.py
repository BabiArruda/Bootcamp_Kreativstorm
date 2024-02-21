#1. Given a text document, write a Python script that extracts all the phone numbers from the text
#using regular expressions. Phone numbers can be in different formats (e.g., (123) 456-7890 or
#123-456-7890).

import re

def phone(string):
    pattern = re.compile(r'^(([0-9]{3}+\-?\s?)|(\([0-9]{3}\)+\-?\s?))+[0-9]{3}\-[0-9]{4}$')
    result = []
    for a in string:
        if re.search(pattern, a):
            result.append(a)

    return result

phones = ['(123) 456-7890', '123-456-7890', '4444-321-2545']
print(phone(phones))