import random as rnd

# generate some random data to play with
rnd.seed(42)
data = rnd.choices(range(100), k=10)

print("Generated data is")
print(data)
   
myMax = data[0]
myMaxIndex = 0
for k, d in enumerate(data):
    if d>myMax:
        myMax = d
        myMaxIndex = k
print(myMaxIndex)
