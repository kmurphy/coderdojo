import random

# initialise game

coins = random.randint(15, 21)
isComputerMove = False
skill = 0.5

print ("Instructions go here ...\n\n")

def getComputerMove(coins):
    if random.random()<skill:   # supersmart (perfect playermode) 
        remainder = coins % 4
        if r==0:
            return random.randint(1,min(2,coins))
        else:
            return remainder
    else:                       # stupid (random mode) 
        return random.randint(1,min(3,coins))
 
def getHumanMove(coins):
    # human move -- need to check input because humans cheat !
    while True:
        move = int(input("How many coins do you want to take (1, 2 or 3)? "))
        if move>coins:
            print ("The pile only contains %s coins. Try again" % coins)
        elif move not in [1,2,3]:
            print ("Expected a move of '1', '2' or '3'.")
        else:
            break
    return move


# play the game

while coins>0:
    
    print("The pile contains %s coins." % coins)
    
    if isComputerMove:
        move = getComputerMove(coins)
        print ("I'm taking %s coins" % move)
    else:
        move = getHumanMove(coins)
        print ("You're taking %s coins" % move)
                
    coins = coins - move
    isComputerMove = not isComputerMove                                 

# output result of game

if isComputerMove:
    print ("\nYou moved last. you win")
else:
    print ("\nI moved last. you lose")
    

