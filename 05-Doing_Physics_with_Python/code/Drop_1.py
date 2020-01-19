y = 25
v = 0
a = -9.81
t = 0

dt = 0.1

while True:
    
    y = y + v*dt
    v = v + a*dt
    t = t + dt
	
    print("%12.2f %12.2f %12.2f" % (t, y, v))
    
    if y<0: break
    
