while True:
    guess = input()
    if(len(guess)==1 and guess.isalpha):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")