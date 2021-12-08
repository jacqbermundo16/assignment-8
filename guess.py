#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.

#steps
#generate 1 random number from 0-100
import random
print('GUESS THE NUMBER\n The program will generate a random number from 0-100.\n It will give you clues to help you find the exact value.\n "Greater than" means that your input is larger.\n "Less than" means your input is smaller.\n')

def guessNum():
    number = int(random.randint(0,100))
#ask input 
    guess = int(input('Guess the number: '))
    
#evaluate the number, print 'Greater than' if input is greater than the number
    while guess != number:
        if guess > number:
            print('Greater than')
            guess = int(input('Guess the number: '))
    #print 'Less than' if the input is less than the number
        else:
            if guess < number:
                print('Less than')
                guess = int(input('Guess the number: '))
#create a loop until the input is equal to the generated number
    print('You guessed it right')
                

guessNum()