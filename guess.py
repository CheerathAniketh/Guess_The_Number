import random

def guess():
    print("🎯 Welcome to Guess the Number game!")
    print("Rules are simple — guess a number between 0 and 20, and enter it below.")
    print()

    computer = random.choice(range(21))
    print("Alright, let’s go! Type your first guess 👇")
    print()

    while True:
        user = int(input("Number: "))
        if user == computer:
            print("🔥 Success! You've guessed it right!")
            break
        elif user < computer:
            print("Try some higher numbers!")
        elif user > computer:
            print("Not that high, try lower ones!")

guess()
