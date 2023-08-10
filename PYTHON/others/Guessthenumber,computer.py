import random

def gtnc(x):


    print("Welcome to THE GAME.")
    print(f"Enter a number between 1 and {x} so that the computer can guess it.")
    
    lowl=1
    uppl=x

    answer = ""

    while answer != "c":
        # Generate a prediction
        if lowl != uppl:
            predict = random.randint(lowl,uppl)
        else:
            predict = lowl
    
        answer = input(f"My prediction is {predict}. If it's too small enter (S) and if it's too big enter (B) and if it's correct enter (C).").lower()

        if answer == 'b':
         uppl = predict - 1
        elif answer == 's':
         lowl = predict + 1
    
    print(f"The computer has guessed the number {predict} ")


gtnc(10)