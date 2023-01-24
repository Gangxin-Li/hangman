import random
secret_list = ['apple','watermelon','fruits1','fruits2','fruits3']
word = random.choice(secret_list)

    

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {guess} is in the word.".format(guess=guess))
        return True
    else:
        print("Sorry, {guess} is not in the word. Try again.".format(guess=guess))
        return False
def ask_for_input():
    guess = input()
    if len(guess)==1 and guess.isalpha:
        res = check_guess(guess)
while True:
    ask_for_input()

