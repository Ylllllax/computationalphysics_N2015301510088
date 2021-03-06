import math
import numpy as np
import matplotlib.pyplot as pl



def ball(angle):
    
    t=[]
    t.append(0)
    dt=0.01
    B_2_m=4*10**(-5)
    y_0=1*10**4
    g=9.8
    end_time = 200

    angle1=angle*math.pi/180
    x=[]
    v_x=[]
    y=[]
    v_y=[]
    x.append(0)
    y.append(0)
    v_x.append(700*math.cos(angle1))
    v_y.append(700*math.sin(angle1))
    for i in range(int(end_time/dt)):
        m=x[i]+v_x[i]*dt
        x.append(m)
        n=v_x[i]-B_2_m*math.exp(-y[i]/y_0)*((v_x[i]**2+v_y[i]**2)**0.5)*v_x[i]*dt
        v_x.append(n)
        o=y[i]+v_y[i]*dt	
        y.append(o)
        p=v_y[i]-g*dt-B_2_m*math.exp(-y[i]/y_0)*((v_x[i]**2+v_y[i]**2)**0.5)*v_y[i]*dt
        v_y.append(p)
        if o <= 0 :
            break
    pl.plot(x,y,label=" %s $^\circ$" %angle)

pl.figure(figsize=(10,6))
angle=[]
for i in range(3):
    a=(35+i*15)
    angle.append(a)
    ball(angle[i])
pl.xlabel("x(m)")
pl.ylabel("y(m)")
pl.xlim(0,30000)
pl.ylim(0,15000)
pl.legend()
pl.show()
