#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.

#steps
#generate 1 random number from 0-100
import random

def guessNum():
    number = int(random.randint(0,100))
#ask input 
    guess = int(input('Guess the number: '))
    print(guess)
#evaluate the number, print 'Greater than' if input is greater than the number
#print 'Less than' if the input is less than the number
#create a loop until the input is equal to the generated number

guessNum()