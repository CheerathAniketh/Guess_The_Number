import random

def guess():
    print("Welcome to Guess the number game!")
    print("Rules of this game is simple you need to guess a number between 0-20 and enter that below")

    computer = random.choice(range(21))
    print("Type your guess below")


    while True:
        user = int(input("Number "))
        if user == computer:
            print("Success you've guessed it right ")
            break
        elif user < computer:
            print("Try some higer numbers")
        elif user > computer:
            print("Not that high try some lower numbers")
            
guess()
