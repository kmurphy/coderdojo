import random as rnd

# generate some random data to play with
rnd.seed(42)
data = rnd.choices(range(100), k=10)

print("Generated data is")
print(data)
   
myMax = 0
mySecondMax = 0
for d in data:
    if d>myMax:
        mySecondMax = myMax
        myMax = d
    elif d>mySecondMax:
        mySecondMax = d
print(mySecondMax)

    