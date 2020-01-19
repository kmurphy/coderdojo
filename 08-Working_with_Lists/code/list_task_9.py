import random as rnd

# generate some random data to play with
rnd.seed(42)
data = rnd.choices(range(100), k=10)

print("Generated data is")
print(data)
   
total = 0
for d in data:
    total = total + d
print(total)
