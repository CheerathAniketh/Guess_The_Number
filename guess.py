import random

def guess():
    print("Welcome to Guess the number game!")

    computer = random.choice(range(21))


    while True:
        user = int(input("Guess the number "))

        if user == computer:
            print("Success you've guessed it rigth ")
            break
                 
        elif user < computer:
            print("Try some higer numbers")
            

        elif user > computer:
            print("Not that high try some lower numbers")
            
        
        
        


guess()