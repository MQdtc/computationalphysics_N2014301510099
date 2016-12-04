# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:49:05 2016

@author: MQdtc
"""
import math
import matplotlib.pyplot as plt
GM = 4 * (math.pi**2)
class Hyperion:
    def __init__(self, eccentricity = 0.5, time = 10.0, dt = 0.0001, theta_1 = 0, theta_2 = 0.01, omega_1 = 0, omega_2 = 0):
        self.theta1 = theta_1
        self.theta2 = theta_2
        self.omega1 = omega_1
        self.omega2 = omega_2
        self.e = eccentricity
        self.x_c = 1 * (1 + eccentricity)
        self.y_c = 0
        self.v_x0 = 0
        self.v_y0 = math.sqrt((GM * (1 - eccentricity))/(1 * (1 + eccentricity)))
        self.X = [self.x_c]
        self.Y = [self.y_c]
        self.V_x = [self.v_x0]
        self.V_y = [self.v_y0]
        self.dt = dt
        self.time = time
        self.Theta1 = [self.theta1]
        self.Theta2 = [self.theta2]
        self.Omega1 = [self.omega1]
        self.Omega2 = [self.omega2]
        self.Deltatheta = [self.theta2 - self.theta1]
        self.Time = [0]
        return None
    def calculate(self):
        while (self.Time[-1] < self.time):
            rc = math.sqrt(self.X[-1]**2 + self.Y[-1]**2)
            newVx = self.V_x[-1] - (GM * self.X[-1]/rc**3) * self.dt
            self.V_x.append(newVx)
            newX = self.X[-1] + newVx * self.dt
            newVy = self.V_y[-1] - (GM * self.Y[-1]/rc**3) * self.dt
            self.V_y.append(newVy)
            newY = self.Y[-1] + newVy * self.dt
            self.X.append(newX)
            self.Y.append(newY)
            newW1 = self.Omega1[-1] - 3 * GM/(rc**5) * (self.X[-1] * math.sin(self.Theta1[-1]) - self.Y[-1] * math.cos(self.Theta1[-1])) * (self.X[-1] * math.cos(self.Theta1[-1]) + self.Y[-1] * math.sin(self.Theta1[-1])) * self.dt
            self.Omega1.append(newW1)
            newTheta1 = self.dt * self.Omega1[-1] + self.Theta1[-1]
            newW2 = self.Omega2[-1] - 3 * GM/(rc**5) * (self.X[-1] * math.sin(self.Theta2[-1]) - self.Y[-1] * math.cos(self.Theta2[-1])) * (self.X[-1] * math.cos(self.Theta2[-1]) + self.Y[-1] * math.sin(self.Theta2[-1])) * self.dt
            self.Omega2.append(newW2)
            newTheta2 = self.dt * self.Omega2[-1] + self.Theta2[-1]
#            while newTheta1 > 1 * math.pi:
#                newTheta1 = newTheta1 - 2 * math.pi
#            while  newTheta1 < -1 * math.pi:
#                newTheta1 = newTheta1 + 2 * math.pi 
            self.Theta1.append(newTheta1)
#            while newTheta2 > 1 * math.pi:
#                newTheta2 = newTheta2 - 2 * math.pi
#            while  newTheta2 < -1 * math.pi:
#                newTheta2 = newTheta2 + 2 * math.pi 
            self.Theta2.append(newTheta2)
            Delta = abs(self.Theta2[-1] - self.Theta1[-1])
            self.Deltatheta.append(Delta)
            self.Time.append(self.Time[-1] + self.dt)
        return 0
    def show_results(self):
        plt.semilogy(self.Time, self.Deltatheta)
        plt.legend(loc='upper right',frameon=False,fontsize='small')
        plt.title('Hyperion $\\Delta\\theta$ versus time($e=0.5$)(none reset)')
        plt.xlabel('time(yr)')
        plt.ylabel('$\\Delta\\theta(radians)$')
        plt.xlim(0, 10)
A = Hyperion()
A.calculate()
A.show_results()
plt.show()
