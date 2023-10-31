import random

def select_word():
    word_list = ['apple', 'orange', 'grape', 'peach', 'blueberry']
    word = random.choice(word_list)
    return word

def input_validation():   
    guess = input('Please enter a letter: ')
    if len(guess) == 1:
        if guess.isalpha() == True:
            return print('Good guess!')
        else:
            return print('This is not a letter')
    else:
        raise ValueError("Oops! That is not a valid input.")