# Guess the number

from random import randint

num = randint(1,100)
gues = 1
guess = -1

while (guess != num):
    guess = int(input("Guess the number between 1 to 100 : "))
    if (guess <0):
        print("Please enter a positive number")
    if (guess>num):
        print("Choose lower value !")
        gues += 1
    elif(guess<num and guess>0):
        print("Choose greater value !")
        gues += 1
         
    
print(f"You have guessed number {num} correctly in {gues} guesses")           
