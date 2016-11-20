# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:56:24 2016

@author: MQdtc
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define the positions of z, r is variable
class phase_space:
    def __init__(self,r):
        self.x=[1]
        self.y=[0]
        self.z=[0]
        self.vx=[0]
        self.vy=[0]
        self.vz=[0]
        self.t=[0]
        self.dt=0.0001
        self.sigma=10
        self.b=8/3
        self.r=r
    def calculate(self):
        for i in range(500000):
            self.vx.append(self.sigma*(self.y[-1]-self.x[-1]))
            self.vy.append(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])
            self.vz.append(self.x[-1]*self.y[-1]-self.b*self.z[-1])
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.z.append(self.z[-1]+self.vz[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return self.x,self.y,self.z
#A=phase_space(25)
#A.calculate()
#fig=plt.figure()
#a=fig.add_subplot(111,projection='3d')
#a.plot(A.x,A.y,A.z,"b")
#a.set_xlabel('x')
#a.set_ylabel('y')
#a.set_zlabel('z')
#a.set_title('Phase space plot: 3D version')
#plt.show()

B=phase_space(25)
B.calculate()
plt.plot(B.x, B.y, "b")
plt.xlabel('x')
plt.ylabel('y')
plt.title('y verus x')
plt.show()