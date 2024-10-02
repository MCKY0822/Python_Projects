# Choose Lotto game
# Choose random numbers
# ask user to pick again
#   else exit

import random

while True:

    choices = ('1', '2', '3', '4', '5', '6', '7', '8')
    user = input('***_MABUHAY!!_***\n\nCHOOSE LOTTO GAME.\nINPUT CODE NUMBER ONLY\n\n'
                'EZ 2 Lotto ------- code [1]\n'
                'SWERTRES Lotto --- code [2]\n'
                '4D Lotto --------- code [3]\n'
                '6D Lotto --------- code [4]\n'
                'Mega Lotto 6/45 -- code [5]\n'
                'Super Lotto 6/49 - code [6]\n'
                'Grand Lotto 6/55 - code [7]\n'
                'Ultra Lotto 6/58 - code [8]\n\n'
                'CODE: ')

    if user == '1': # EZ 2 Lotto
        numbers = random.sample(range(1, 31),2)
        print('\nEZ 2 Lotto - Lucky numbers:', numbers)

    elif user == '2': # SWERTRES Lotto
        first = random.randint(0, 9)
        second = random.randint(0, 9)
        third = random.randint(0, 9)
        print('\nSWERTRES Lotto - Lucky numbers:',[ first, second, third ])

    elif user == '3': # 4D Lotto
        first = random.randint(0000, 9999)
        print('\n4D Lotto - Lucky number:',[ first ])

    elif user == '4': # 6D Lotto
        first = random.randint(0, 9)
        second = random.randint(0, 9)
        third = random.randint(0, 9)
        forth = random.randint(0, 9)
        fifth = random.randint(0, 9)
        sixth= random.randint(0, 9)
        print('\n6D Lotto - Lucky numbers:',[ first, second, third, forth, fifth, sixth ])

    elif user == '5': # Mega Lotto 6/45
        numbers = random.sample(range(1, 45),6)
        print('\nMega Lotto 6/45 - Lucky numbers:', numbers)

    elif user == '6': # Super Lotto 6/49
        numbers = random.sample(range(1, 49),6)
        print('\nSuper Lotto 6/49 - Lucky numbers:', numbers)

    elif user == '7': # Grand Lotto 6/55
        numbers = random.sample(range(1, 55),6)
        print('\nGrand Lotto 6/55 - Lucky numbers:', numbers)
        
    elif user == '8': # Ultra Lotto 6/58
        numbers = random.sample(range(1, 58),6)
        print('\nUltra Lotto 6/58 - Lucky numbers:', numbers)

    else:
        print('\nInvalid choice. Please put valid code number only.')
        continue

    pick_again = input('\nPick Again? (yes/no): ').lower()

    if pick_again != 'yes':
        break

print('\nGood luck!')