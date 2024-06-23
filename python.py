import sys
import random

number = random.randint(1,15)

Guess1 = int(input("Enter your Number Between 1 to 15\n"))

if(Guess1 == number):
    print("You Guessed in First Trail!! it's Awsome\n")
    sys.exit()

elif(number < Guess1):
    print("Number is too high. Try you have Another Two Chances......")

else:
    print("Number is too low. Try you have Another Two Chances......")

 
 
Guess2 = int(input("Enter your Number Between 1 to 15\n"))

if(Guess2 == number):
    print("You Guessed in Second Trail!! it's Nice\n")
    sys.exit()

elif(number < Guess2):
    print("Number is too high. Try you have Another one Chance......")
    
else:
    print("Number is too low. Try you have Another one Chance......")


Guess3 = int(input("Enter your Number Between 1 to 15\n"))

if(Guess3 == number):
    print("You Guessed it !! it's cool\n")
    sys.exit()

elif(number < Guess3):
    print("Number is too high. You Lost the Game...Better Luck Next Time")

else:
    print("Number is too low. You Lost the Game...Better Luck Next Time")



        
