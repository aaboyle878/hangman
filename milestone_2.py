import random

word_list = ['apple', 'orange', 'grape', 'peach', 'blueberry']
word = random.choice(word_list)
guess = input('Please enter a letter: ')
if guess.len() == 1:
    if guess.isalpha() == True:
        print('Good guess!')
    else:
        print('This is not a letter')
else:
    print('Oops! That is not a valid input.')



print(word_list)
print(word)
print(guess)
