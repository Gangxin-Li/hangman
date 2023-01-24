import random
secret_list = ['apple','watermelon','fruits1','fruits2','fruits3']
word = random.choice(secret_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {guess} is in the word.".format(guess=guess))
    else:
        print("Sorry, {guess} is not in the word. Try again.".format(guess=guess))

def ask_for_input():
    while True:
        guess = input()
        if len(guess)==1 and guess.isalpha:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()

    

