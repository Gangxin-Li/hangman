import random
class Hangman():
    def __init__(self,word_list,num_list=5) -> None:
        self.word_list = ['apple','watermelon','fruits1','fruits2','fruits3']
        self.word = random.choice(word_list)
        self.word_guessed = ['_','_','_','_','_']
        self.num_letters = 0

        self.num_lives = 0
        self.list_of_guesses=[]