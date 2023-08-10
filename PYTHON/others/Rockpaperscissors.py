import random


def play():

    User = input("Choose one option: 'R' for rock, 'P' for paper, and 'S' for scissors.\n").lower()
    Computer = random.choice(['p','r','s'])
    # if Computer =='p':
    #  print('paper')
    # elif Computer =='r':
    #  print('rock')
    # elif Computer == 's':
    #  print('scissors') 

    if User == Computer:
        return 'A tie!'
    
    if wontheplayer(User,Computer):
        return 'You won!'
    
    return 'You lost!'


def wontheplayer(player,opponent):
    # Return True if the player wins.
    # R > S,     P > R,     S > P
    if ((player == 'r' and opponent == 's') 
        or (player == 'p' and opponent == 'r') 
        or (player == 's' and opponent == 'p')):
        return True
    else: 
        return False
    

print(play())
    



