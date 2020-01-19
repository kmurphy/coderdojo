import random

secret = random.randint(1, 20)

print("I have picked a secret number between 1 and 20.")
print("You have 5 guesses to figure it out ...")

for k in range(5):
    
    guess = int(input("Enter your guess: "))
    
    if guess == secret:
        print("Well done!")
        break
                
    if guess < secret:
        print("Go higher")
    else:
        print("Go lower")
        
else:
    print("You only get 5 tries. I win!")

        
