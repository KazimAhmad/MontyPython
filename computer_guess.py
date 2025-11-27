import random
upperLimit = 10

def computer_guess():
    global upperLimit

    low = 1
    high = upperLimit
    feedback = ''

    while feedback != 'c':
        if low != high:
             guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too  high (H), too low (L) or correct (C)?: ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    again = input(print(f'the computer guessed the number {guess}, correctly, play again? (Y/N)'))
    if again == 'Y':
        upperLimit = upperLimit + 10
        computer_guess()

computer_guess()