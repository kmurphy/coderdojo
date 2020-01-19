t = 0
y = 10
v = 16
a = -9.81

dt = 0.01

#import pygal                                                       
#bar_chart = pygal.Bar()                                            
#bar_chart.add('Fibonacci', [0, 1, 6, 2, 3, 5, 8, 13, 21, 34, 55])

#bar_chart.render_in_browser()



print ("%12s %12s %12s" % ("time", "position", "velocity"))
print ("-" * 39)


c = 0
while y>0:
    
    if c%20==0:
        print ("%12.3f %12.3f %12.3f" % (t,y,v))
    c = c + 1

    y = y + v*dt
    v = v + a*dt
    t = t + dt


import pygal
piechart = pygal.Pie()
piechart.render()