import random

def play():
    user = input(" 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    
    if is_win(user, computer):
        return 'won'
    
    return 'lost'

def is_win(player, opp):
    playerRoppS = player == 'r' and opp == 's'
    playerSoppP = player == 's' and opp == 'p'
    playerPoppR = player == 'p' and opp == 'r'

    if playerRoppS or playerSoppP or playerPoppR:
        return True

print(play())