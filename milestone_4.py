import random
class Hangman():
    def __init__(self,word_list,num_lives=5) -> None:
        
        self.word = random.choice(word_list)
        self.word_guessed = ['_','_','_','_','_']
        self.num_letters = 0
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses=[]