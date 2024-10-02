import random

def emojiConverter(choice):
        emojis = {'rock': '🪨', 'paper': '📃', 'scissors': '✂'}
        return emojis.get(choice, choice)


while True:

    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:

        player = input('rock, paper or scissors?: ').lower()
        if player not in choices:
            print('Invalid choice')

    if player == computer:
        print('Player: ', emojiConverter(player))
        print('Computer: ', emojiConverter(computer))
        print("It's a TIE!")

    elif player == 'rock':
        if computer == 'scissors':
            print('Player: ', emojiConverter(player))
            print('Computer: ', emojiConverter(computer))
            print("You WIN!")
        if computer == 'paper':
            print('Player: ', emojiConverter(player))
            print('Computer: ', emojiConverter(computer))
            print("You LOSE!")

    elif player == 'paper':
        if computer == 'rock':
            print('Player: ', emojiConverter(player))
            print('Computer: ', emojiConverter(computer))
            print("You WIN!")
        if computer == 'scissors':
            print('Player: ', emojiConverter(player))
            print('Computer: ', emojiConverter(computer))
            print("You LOSE!")

    elif player == 'scissors':
        if computer == 'paper':
            print('Player: ', emojiConverter(player))
            print('Computer: ', emojiConverter(computer))
            print("You WIN!")
        if computer == 'rock':
            print('Player: ', emojiConverter(player))
            print('Computer: ', emojiConverter(computer))
            print("You LOSE!")

    play_again = input('Play Again? (yes/no): ').lower()

    if play_again != 'yes':
        break

print('Good bye!')