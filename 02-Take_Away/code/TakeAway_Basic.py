
# initialise game
import random
coins = random.randint(15, 25)
isComputerMove = False

print ("Instructions go here ...\n\n")

# play the game

while coins>0:
    
    print("The pile contains %s coins." % coins)
    
    if isComputerMove:
        move = 1
        print ("I'm taking %s coins" % move)
    else:
        move = int(input("How many coins do you want? "))
        print ("You're taking %s coins" % move)
                
    coins = coins - move
    
    isComputerMove = not isComputerMove                                 

# output result of game

if isComputerMove:
    print ("\nYou moved last. you win")
else:
    print ("\nI moved last. you lose")
    

