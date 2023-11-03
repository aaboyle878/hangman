import random

class Hangman():
    def __init__(word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        word = random.choice(word_list)
        word_guessed = ['_'] * len(word)
        num_letters = len(set(list(word)))
        list_of_guesses = []
