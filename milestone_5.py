import random


def play_game(word_list):
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_lives == 0:
            return print("You lost")
        elif game.num_lives > 0 and game.num_letters > 0:
            game.ask_for_input()
        else:
            return print("Congratulation, You have won!")

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.list_of_guesses = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(list(self.word)))
        print(f"The Mystery word has {self.num_letters} characters")
        
    def ask_for_input(self):
        while True:
            print(self.word_guessed)
            guess = input('Please enter a single letter: ')
            guess = guess.lower()
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                break
        self.check_guess(guess)
    
    def check_guess(self,guess):
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

if __name__ == "__main__":
    play_game(['apple', 'orange', 'grape', 'peach', 'blueberry'])
