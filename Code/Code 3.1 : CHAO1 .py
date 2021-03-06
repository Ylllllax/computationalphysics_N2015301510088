import matplotlib.pyplot as plt
import numpy as np
import math


class chao(object):
    def __init__(self,FD):
        self.theta, self.omg, self.t = [0.2], [0.0], [0.0]
        self.l, self.g, self.dt, self.time, self.q, self.OMGD=9.8, 9.8, 0.04, 60.0, 0.5, 2./3.
        self.F_D=FD
        self.n=int(self.time/self.dt)
        self.I=range(self.n)
    def calculate(self):
        for i in self.I:
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q*self.omg[i]+self.F_D*math.sin(self.OMGD*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
                self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
                self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta,label='$F_D$='+str(self.F_D))
    def plot_omega(self,_ax):
        _ax.plot(self.t,self.omg,label='$F_D$='+str(self.F_D))

fig= plt.figure(figsize=(14,7))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

comp= chao(0.0)
comp.calculate()
comp.plot_theta(ax1)
comp.plot_omega(ax2)

comp=chao(0.5)
comp.calculate()
comp.plot_theta(ax1)
comp.plot_omega(ax2)

comp=chao(1.2)
comp.calculate()
comp.plot_theta(ax1)
comp.plot_omega(ax2)

ax1.set_title(r'$\theta$'+' versus time',fontsize=14)
ax2.set_title(r'$\omega$'+' versus time',fontsize=14)
ax1.set_xlabel('time(s)',fontsize=14)
ax1.set_ylabel(r'$\theta$'+'(radians)',fontsize=14)
ax2.set_xlabel('time(s)',fontsize=14)
ax2.set_ylabel(r'$\omega$'+'(radians/s)',fontsize=14)
ax1.legend(fontsize=12,loc='best')
ax2.legend(fontsize=12,loc='best')
plt.show(fig)
