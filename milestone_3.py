while(True):
    guess = input("Guessing a letter")
    if(len(guess)==1 and guess.isalpha):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")