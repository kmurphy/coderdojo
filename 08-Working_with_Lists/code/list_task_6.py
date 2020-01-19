import random as rnd

# generate some random data to play with
rnd.seed(42)
data = rnd.choices(range(100), k=10)

print("Generated data is")
print(data)
   
myMax = data[0]
myMin = data[0]
for d in data:
    if d>myMax:
        myMax = d
    if d<myMin:
        myMin = d
print(myMax-myMin)
