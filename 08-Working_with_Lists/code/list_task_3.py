import random as rnd

# generate some random data to play with
rnd.seed(42)
data = rnd.choices(range(100), k=10)

print("Generated data is")
print(data)
   
for k in range(len(data)):
    print(data[len(data)-1-k])