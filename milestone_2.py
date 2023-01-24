import random
word_list = ['apple','watermelon','fruits1','fruits2','fruits3']
word = random.choice(word_list)
print(word_list)
print(word)


guess = input()

if(len(guess)==1 and guess.isalpha):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")