# setup physics problem
y = 25
v = 0
a = -9.81
t = 0

dt = 0.1
output_dt = 0.1

# print header
print("%12s %12s %12s" % ("time", "height", "velocity"))
print("="*39)

# do computation
while True:
    
    if  abs(int(t/output_dt)-t/output_dt)<output_dt/2:
        print("%12.2f %12.2f %12.2f" % (t, y, v))

    y = y + v*dt
    v = v + a*dt
    t = t + dt
    
    if y<0: break
    
# output final data
print("The ball was falling for %.2f seconds." % t)
print("At impact ball was moving at %.2f metres per second." % -v)
