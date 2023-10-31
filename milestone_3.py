from milestone_2 import select_word

chosen_word = select_word()

def ask_for_input():
    while True:
        guess = input('Please enter a single letter: ')
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


def check_guess(guess):
    guess = guess.lower()
    if guess in chosen_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()