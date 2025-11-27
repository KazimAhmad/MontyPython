import random
upperLimit = 10

def computer_guess():
    global upperLimit
    upperLimit = int(input('making me guess between 1 and ? '))
    low = 1
    high = upperLimit
    feedback = ''

    while feedback != 'c':
        if low != high:
            middle = (low + high) / 2
            guess = int(middle)
        else:
            guess = low
        feedback = input(f'is {guess} too  high (H), too low (L) or correct (C)?: ').lower()
        if feedback == 'h':
            high = guess
        elif feedback == 'l':
            low = guess

    again = input(print(f'the computer guessed the number {guess}, correctly, play again? (Y/N)'))
    if again == 'Y':
        computer_guess() 

computer_guess()