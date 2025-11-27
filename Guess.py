import random

upperLimit = 10
def guessTheNumber():
    global upperLimit
    random_number = random.randint(1, upperLimit)
    guess = 0

    while (guess != random_number):
        guess = int(input(f'Guess a number between 1 and {upperLimit}: '))
        if guess < random_number:
            print('Sorry, guess again, Too low')
        elif guess > random_number:
            print('Sorry, guess again, Too high')
    again = input(print('You guessed the number correctly, wanna play again? (Y/N)'))
    if again == 'Y':
        upperLimit = upperLimit + 10
        guessTheNumber()

guessTheNumber()
        