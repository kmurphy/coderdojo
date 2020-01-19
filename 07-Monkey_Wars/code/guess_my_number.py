secret = 17

print ("Hi, I have picked a random number between 1 and 20. Can you guess it?")

for k in range(5):
    guess = int(input("Enter your guess human: "))
    if guess<secret:
        print("Ha, too low!")
    elif guess>secret:
        print("Ha, too high!")
    else:
        print("Blast! you got it right!")
        break
        
print("Game Over")