import matplotlib.pyplot as plt
import numpy as np


class osci(object):
    def __init__(self, _theta0=0.2, _omg0=0, _t0=0., _l=1., _g=9.8, _dt=0.01, _time=10.):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[i]+self.dt)
            self.omg.append(self.omg[i]-self.g/self.l*self.theta[i]*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta)

        
fig= plt.figure(figsize=(20,8))
ax1 = plt.subplot(121)


comp= osci()
comp.calculate()
comp.plot_theta(ax1)

ax1.set_title('Simple Pendulum - Euler-Cromer method',fontsize=14)
ax1.set_xlabel('time/s',fontsize=14)
ax1.set_ylabel(r'$\theta$'+'(rad)',fontsize=14)
ax1.legend(fontsize=12,loc='best')
plt.show(fig)
