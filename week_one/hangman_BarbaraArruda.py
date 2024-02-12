'''
The hangman game is a word guessing game where the player is given a word and
has to guess the letters that make up the word.
The player is given a certain number of tries (no more than 6 wrong guesses are
allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.
Used letters:
Word: _ _ _ _
Guess a letter: a

You have 6 tries left.
Used letters: a
Word: _ a _ a
Guess a letter: j

You have 6 tries left.
Used letters: j a
Word: j a _ a
Guess a letter: v
You guessed the word java !
'''
def find_letter(string):
    count = 6
    used_letters = []
    guess = '_'*(len(string))
    while count > 0:
        char = input('Guess a letter: ').lower()
        used_letters.append(char)
        if char in string:
            for num, letter in enumerate(string):
                if letter == char:
                    templist = list(guess)
                    templist[num] = char
                    guess = ''.join(templist)
        else:
            count -=1
        if count != 0 and guess != string:
            print(f'You have {count} tries left.')
            print('Used letters:', *used_letters)
            print('Word: ' + guess)
        elif guess != string and count == 0:
            print('You lose')
        else:
            print(f'You guessed the word {guess} !')
            break


word = input('Enter the word that we should guess \n').lower()
find_letter(word)