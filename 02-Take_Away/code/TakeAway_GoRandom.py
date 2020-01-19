import random


def getComputerMove(coins):
    move = random.randint(1,3)
    return move

def getHumanMove(coins):
    # human move -- need to check input bacuase human cheat !
    while True:
        move = int(input("How many coins do you want to take (1, 2 or 3)? "))
        if move>coins:
            print ("The pile only contains %s coins. Try again" % coins)
        elif move not in [1,2,3]:
            print ("Expected a move of '1', '2' or '3'.")
        else:
            break
    return move

# initialise game

coins = random.randint(15, 21)
isComputerMove = False

# output instructions

print ("Instructions go here ...\n\n")

# play the game

while coins>0:
    
    print("The pile contains %s coins." % coins)
    
    if isComputerMove:
        move = getComputerMove(coins)
        print ("I'm taking %s coins" % move)
    else:
        move = getHunmanMove(coins)
        print ("You're taking %s coins" % move)
                
    coins = coins - move
    isComputerMove = not isComputerMove                                 

# output result of game

if isComputerMove:
    print ("\nYou moved last. you win")
else:
    print ("\nI moved last. you lose")
    

