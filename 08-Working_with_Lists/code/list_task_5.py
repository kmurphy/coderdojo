import random as rnd

# generate some random data to play with
rnd.seed(42)
data = rnd.choices(range(100), k=10)

print("Generated data is")
print(data)
   
myMin = data[0]
for d in data:
    if d<myMin:
        myMin = d
print(myMin)
