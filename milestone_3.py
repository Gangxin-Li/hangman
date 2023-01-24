import random
secret_list = ['apple','watermelon','fruits1','fruits2','fruits3']
word = random.choice(secret_list)
while True:
    guess = input()
    if guess in word:
        print("Good guess! {guess} is in the word.".format(guess=guess))
        break
    else:
        print("Sorry, {guess} is not in the word. Try again.".format(guess=guess))




