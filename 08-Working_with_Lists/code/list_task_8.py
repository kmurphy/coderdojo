import random as rnd

# generate some random data to play with
rnd.seed(42)
data = rnd.choices(range(100), k=10)

print("Generated data is")
print(data)
   
myMin = data[0]
myMinIndex = 0
for k, d in enumerate(data):
    if d<myMin:
        myMin = d
        myMinIndex = k
print(myMinIndex)
