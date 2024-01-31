# 2. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

# Score   Grade
# >= 0.9  A
# >= 0.8  B
# >= 0.7  C
# >= 0.6  D
#  < 0.6  F

score = input('Enter your score\n')
try:
    score=float(score)
    if score >= 0.9 and score <= 1:
        print('Your Grade is A')
    elif score < 0.9 and score >=0.8 :
        print('Your Grade is B')
    elif score < 0.8 and score >=0.7 :
        print('Your Grade is C')
    elif score < 0.7 and score >=0.6 :
        print('Your Grade is D')
    elif score < 0.6 and score >=0:
        print('Your Grade is F')
    else:
        print('Insert a value score')
except Exception:
    print('Insert a valid number')