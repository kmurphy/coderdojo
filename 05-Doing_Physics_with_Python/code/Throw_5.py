# setup physics problem
y = 1.3
v = 25
a = -9.81
t = 0

dt = 0.001
output_dt = 0.01

max_height = 0
time_of_max_height = 0

# print header
print("%12s %12s %12s" % ("time", "height", "velocity"))
print("="*39)

# do computation
while True:
    
    if abs(int(t/output_dt)-t/output_dt)<dt:
        print("%12.3f %12.2f %12.2f" % (t, y, v))

    y = y + v*dt
    v = v + a*dt
    t = t + dt
    
    if y>max_height:
        max_height = y
        time_of_max_height = t
        
    if y<0: break
    
# output final data
print("The ball was in the air for %.2f seconds." % t)
print("At impact ball was moving at %.2f metres per second." % -v)
print("Maximum height of ball was %.2f metres." % max_height)

print("Maximum height occured at time %.2f seconds." % time_of_max_height)


