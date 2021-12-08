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
import random
#ask for 3 numerical inputs (0-9)
def lottery():
    num1_ = int(input('Enter 1st number: '))
    num2_ = int(input('Enter 2nd number: '))
    num3_ = int(input('Enter 3rd number: '))
    inputs = f'{num1_}{num2_}{num3_}'


#create a function that generates 3 random numbers(0-9) - save as winning numbers
    win1_ = int(random.randint(0,9))
    win2_ = int(random.randint(0,9))
    win3_ = int(random.randint(0,9))
    results = f'{win1_}{win2_}{win3_}'

#evaluate the numbers; if all numbers matched display 'winner'
    matched = 0
    for i in inputs:
        for r in results:
            if i == r:
                matched = matched + 1

    if matched == 3:
        print('\nWinner')
    #if not, display 'you loss'
    else:
        print(f'\nYou loss\nWinning numbers are {win1_}, {win2_}, and {win3_}')

#aks the player after each game if they will play again (y/n are the options)
    end = 'yes'
    ans = input('Try again y/n: ')
    end = ans
    # 'y' = another game
    # 'n' = exit game
    while end[0] == 'y':
        num1_ = int(input('\nEnter 1st number: '))
        num2_ = int(input('Enter 2nd number: '))
        num3_ = int(input('Enter 3rd number: '))
        inputs = f'{num1_}{num2_}{num3_}'

        win1_ = int(random.randint(0,9))
        win2_ = int(random.randint(0,9))
        win3_ = int(random.randint(0,9))
        results = f'{win1_}{win2_}{win3_}'
    
        matched = 0
        for i in inputs:
            for r in results:
                if i == r:
                    matched = matched + 1

        if matched == 3:
            print('\nWinner')
        #if not, display 'you loss'
        else:
            print(f'\nYou loss\nWinning numbers are {win1_}, {win2_}, and {win3_}')
            
        
        ans = input('Try again y/n: ')
        end = ans


lottery()

        



