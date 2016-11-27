# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 22:09:05 2016

@author: MQdtc
"""
import math
import matplotlib.pyplot as plt
GM = 4 * (math.pi**2)
class Precession_of_Mercury:
    def __init__(self, radius = 0.39, eccentricity = 0.206, time = 2., dt = 0.0001, alpha = 0.0008):
        self.alpha = alpha
        self.e = eccentricity
        self.a = radius
        self.x_0 = self.a * (1 + eccentricity)
        self.y_0 = 0
        self.v_x0 = 0
        self.v_y0 = math.sqrt((GM * (1 - eccentricity))/(self.a * (1 + eccentricity)))
        self.X = [self.x_0]
        self.Y = [self.y_0]
        self.V_x = [self.v_x0]
        self.V_y = [self.v_y0]
        self.T = [0]
        self.dt = dt
        self.time = time
        self.ThetaPrecession = []
        self.TimePrecession = []
        return None
    def calculate(self):
        while (self.T[-1] < self.time):
            r = math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx = self.V_x[-1] - (GM * (1 + self.alpha/r**2)) * (self.X[-1]/r**3) * self.dt
            newX = self.X[-1] + newVx * self.dt
            newVy = self.V_y[-1] - (GM * (1 + self.alpha/r**2)) * (self.Y[-1]/r**3) * self.dt
            newY = self.Y[-1] + newVy * self.dt
            if abs(newX*newVx+newY*newVy) < 0.0014 and r < self.a:
                theta = math.acos(self.X[-1]/r) * 180/math.pi
                if (self.Y[-1]/r) < 0:
                    theta = 360 - theta
                theta = abs(theta - 180)
                self.ThetaPrecession.append(theta)
                self.TimePrecession.append(self.T[-1])
            self.V_x.append(newVx)
            self.V_y.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.T.append(self.T[-1] + self.dt)
        return 0
    def show_results(self):
        plt.plot(self.X,self.Y)
        plt.legend(loc='upper right',frameon=False,fontsize='small')
        plt.grid(True)
        plt.title('The precession of Mercury with $\\alpha=0.206$')
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.xlim(0.2,0.4)
        plt.ylim(0.2,0.4)
#        plt.scatter(0,0)
        
        return 0
    def orientation(self):
        plt.plot(self.TimePrecession,self.ThetaPrecession)
        plt.scatter(self.TimePrecession,self.ThetaPrecession)
        plt.legend(loc='upper right',frameon=False,fontsize='xx-small')
        plt.grid(True)
        plt.xlabel('$time(yr)$')
        plt.ylabel('$\\theta(degrees)$')
        print self.ThetaPrecession
        print self.TimePrecession
        return 0
A = Precession_of_Mercury()
A.calculate()
A.orientation()
plt.show()
