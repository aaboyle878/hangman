import random

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.list_of_guesses = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(list(self.word)))

    def ask_for_input(self):
        while True:
            guess = input('Please enter a single letter: ')
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                break
        self.check_guess(guess)
    
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            counter = 0
            for letter in self.word:
                if guess  == letter:
                    self.word_guessed[counter] = guess
                    counter += 1
                    pass
                else:
                    counter += 1
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
                

game1 = Hangman(['apple', 'orange', 'grape', 'peach', 'blueberry'])
game1.ask_for_input()
