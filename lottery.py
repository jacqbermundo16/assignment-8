#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

#steps
# display the name of the game and instructions
print('LOTTERY')
print(f' The program will ask you to input 3 numbers from 0-9.\n If you got all the numbers matched, you win.\n Results will be printed below.\n It will also ask if you want to play again.\n')
#ask for 3 numerical inputs (0-9)
def ask3Nums():
    num1_ = int(input('Enter 1st number: '))
    num2_ = int(input('Enter 2nd number: '))
    num3_ = int(input('Enter 3rd number: '))
    return num1_, num2_, num3_

#create a function that generates 3 random numbers(0-9) - save as winning numbers
import random

def winningNums():
    win1_ = int(random.randint(0,9))
    win2_ = int(random.randint(0,9))
    win3_ = int(random.randint(0,9))
    return win1_, win2_, win3_

#evaluate the numbers; if all numbers matched display 'winner'
#if not, display 'you loss'
#aks the player after each game if they will play again (y/n are the options)
# 'y' = another game
# 'n' = exit game

num1, num2, num3 = ask3Nums()
win1, win2, win3 = winningNums()
print(num1,num2, num3)
print(win1, win2, win3)