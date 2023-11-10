import random


class Hangman():
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
    word_list: list
        List of words to be used in the game

    Methods:
    -------
    ask_for_input(self)
        Asks the user for a letter.
    check_guess(self,guess)
        Checks if the letter is in the word.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.list_of_guesses = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(list(self.word)))
        print(f"The Mystery word has {self.num_letters} characters")
        
    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
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
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''
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

#will ask the player for input while they still have lives and have not yet won the game
def play_game(word_list):
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_lives == 0:
            return print("You lost")
        elif game.num_lives > 0 and game.num_letters > 0:
            game.ask_for_input()
        else:
            return print("Congratulation, You have won!")

if __name__ == "__main__":
    play_game(['apple', 'orange', 'grape', 'peach', 'blueberry'])
