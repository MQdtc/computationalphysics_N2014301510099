# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 23:16:28 2016

@author: MQdtc
"""
import math
import matplotlib.pyplot as plt
import numpy as np
class pendulum():
    def __init__(self, FD, driveOmega, T = 4500, theta = 0.2, omega = 0, damping = 0.5, step = 1000):
        self.step = step
        self.q = damping
        self.Omega = driveOmega
        self.theta = [theta]
        self.alltheta = [theta]
        self.Poincaretheta = [theta]
        self.Bifurcationtheta = [theta]
        self.omega = [omega]
        self.Poincareomega = [omega]
        self.period = 2 * math.pi/self.Omega
        self.T = T
        self.t = [0]
        self.dt = self.period/self.step
        self.drive = FD
        return None
    def calculate(self):
        while (self.t[-1] < self.T):
            omega = self.omega[-1] -(math.sin(self.theta[-1]) + self.q * self.omega[-1]\
            - self.drive * math.sin(self.Omega * self.t[-1])) * self.dt
            self.omega.append(omega)
            theta = self.theta[-1] + self.omega[-1] * self.dt
         #经过建议，改为用while语句来修正theta的值
            while theta < -math.pi:
                theta = theta + 2 * math.pi
            while theta > math.pi:
                theta = theta - 2 * math.pi
            self.theta.append(theta)
            t = self.t[-1] + self.dt
            self.t.append(t)
    def Poincare(self):
        for i in range(1000):
            self.Poincareomega.append(self.omega[1000 * i - 1])
            self.Poincaretheta.append(self.theta[1000 * i - 1])
        plt.scatter(self.Poincaretheta, self.Poincareomega, s=0.1, label='$F_{D}$=1.2')
        plt.xlabel('$\\theta$ (radians)')
        plt.ylabel('$\\omega$(radians/s)')   
        plt.xlim(-4,4)
        plt.ylim(-2,1)    
        plt.title('$\\omega$ versus $\\theta$')
        plt.legend(loc='upper right',frameon = True)
        plt.grid(True)
        plt.show()
#A = pendulum(FD=1.2, driveOmega = 2.0/3)
#A.calculate()
#A.Poincare()
#This section is used to caluclate and store the data of theta after 300 periods of driving foce and a fixed driving force
def Bifurcation_Plot(init_NUMBER = 0, F_D = 1.2, frequency = 2.0/3, color = 'black', slogan = ''):
    B = pendulum(FD = F_D, driveOmega = frequency)
    B.calculate()
    Btheta = []
    for i in range(100):
        Btheta.append(B.theta[(300 + i + init_NUMBER) * B.step])
    Fd = [F_D] * len(Btheta)   
    return (Fd,Btheta)
#Set the intial F_D to be 1.35 and with a interval of 0.001, end with F_D =1.5,other situation can be adapted from this origin program as you wish
FD=[]
Theta=[]
for i in np.arange(1.35,1.5,0.001):
    a=Bifurcation_Plot(F_D=i, frequency=2.0/3)
    FD.extend(a[0])
    Theta.extend(a[1])
plt.scatter(FD, Theta, s=0.1, label=r'$\Omega_D=2/3$')
plt.xlabel('$F_D$ (N)')
plt.ylabel('$\\theta$(radians)') 
plt.xlim(1.34,1.52)
plt.ylim(0,4)
plt.legend()
plt.show()