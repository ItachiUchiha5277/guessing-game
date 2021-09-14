import random
import time
from colorama import Fore, Style

# Fore.BLUE == Blue Text
# Fore.RED == Red Text
# Fore.GREEN == Green Text
# Fore.MAGENTA == Magenta Text
# Fore.YELLOW == Yellow Text
# Fore.WHITE == White Text


# Back.BLUE == Blue Text
# Back.RED == Red Text
# Back.GREEN == Green Text
# Back.MAGENTA == Magenta Text
# Back.YELLOW == Yellow Text
# Back.WHITE == White Text


# Style.DIM == Dim Text
# Style.NORMAL == Normal Text
# Style.BRIGHT == Bold Text

'''
Note: i have used time.sleep() so that the game does not resume in an instant.
I think that a pause of a few milliseconds is nice.
'''

'''
game decides whether to play the game or not
'''
game = True

# final_number generates the number to be guessed
final_number = random.randint(1,20)

while game == True:

    '''
    Here riddle is the hint given to the player.
    It will say the range of the number to be guessed
    '''
    riddle = ''
    
    if final_number <= 5:
        riddle = Fore.BLUE + Style.BRIGHT + 'I am between 0 to 5.'
    elif final_number > 5 and final_number <= 15:
        riddle = Fore.BLUE + 'I am between 5 and 15'
    else:
        riddle = Fore.BLUE + 'I am between 15 and 20'

    '''
    I used a try-except block so that if someone enters a non-int value,
    they can still play the game. basically for handling the ValueError.
    '''
    try:
        time.sleep(0.5)
        user_input = int(input(Style.BRIGHT + Fore.BLUE + f'Hint: {riddle}\nGuess the number: '))

        if user_input > 20:
            print(Style.BRIGHT + Fore.RED + 'Number cannot be greater than 20\n')
            time.sleep(0.4)

        elif user_input == final_number:
            print(Style.NORMAL + Fore.RESET + 'Wait for it...')
            time.sleep(1)
            print(Fore.GREEN + Style.BRIGHT + 'You guessed the number!')
            final_number = random.randint(1,20)
            
            '''
            continue_menu decides whether to ask if the user
            wants to continue playing the game or not.
            '''
            continue_menu = True
            while continue_menu == True:
                time.sleep(0.5)
                ask = input(Style.BRIGHT + Fore.CYAN + 'Enter "yes" or "no" in upper or lower case.\nWould you like to continue? ')

                if ask.lower() == 'yes':
                    continue_menu = False
                    break

                if ask.lower() == 'no':
                    print('Have a great time!')
                    game = False
                    break

                else:
                    print(Style.BRIGHT + Fore.RED + '\nPlease say either "yes" or "no"\n')
                    time.sleep(0.5)
                    continue_menu = True

        else:
            continue
    
    # If someone enters a non-int value, then this error will be printed

    except ValueError:
        print(Style.BRIGHT + Fore.RED + '\nYou must enter a valid digit\n')