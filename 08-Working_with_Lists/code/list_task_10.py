import random as rnd

# generate some random data to play with
rnd.seed(42)
data = rnd.choices(range(100), k=10)

print("Generated data is")
print(data)
   
evenTotal = 0
oddTotal = 0
for d in data:
    if d%2==0:
        evenTotal = evenTotal + d
    else:
        oddTotal = oddTotal + d
print(evenTotal-oddTotal)

# OR

total = 0
for d in data:
    if d%2==0:
        total = total + d
    else:
        total = total - d
print(total)
    