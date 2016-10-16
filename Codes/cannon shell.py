"""
Created on Sun Oct 16 09:46:56 2016

@author: MQdtc
"""

import pylab as pl
import math
print("C/m is around 4 * 10 ^ (-5) on the earth.")
g = input("Please type the gravity acceleration:")  
m = input("Please type the mass of cannon shell:")
ts = input("Please type the time step:")
xi = input("Please type the initial position of x(km):")
yi = input("Please type the initial position of y(km):")
vxi = input("Please type the initial velocity of x(km/s):")
vyi = input("Please type the initial velocity of y(km/s):")
C = input("Please type the drag cofficient:")
T_0 = input("Please type the sea level temperature:")
class cannon_shell:
    def __init__(self, gravity_acceleration = g, mass = m,\
    time_step = ts, initial_x_position = xi,\
    initial_y_position = yi, initial_x_velocity = vxi,\
    initial_y_velocity = vyi, drag_coefficient = C, 
    sea_level_temperature = T_0): 
        self.x = [initial_x_position]
        self.y = [initial_y_position]
        self.vx = [initial_x_velocity]
        self.vy = [initial_y_velocity]
        self.m = mass
        self.g = gravity_acceleration
        self.ts = time_step
        self.C = [drag_coefficient]
        self.T_0 = sea_level_temperature
    def trajectory(self):
        while(self.y[-1] >= 0):
            self.C.append((self.C[-1]/1000) * math.pow(2.5, 1.0 - 0.0065 * self.y[-1]/ self.T_0))
            self.vx.append(self.vx[-1] - self.ts * (self.vx[-1] * self.C[-1] * math.pow(0.5, math.pow(2.0, self.vx[-1]) + math.pow(2.0, self.vy[-1]))/ (1000 * self.m)))
            self.vy.append(self.vy[-1] - (self.g/ 1000) * self.ts - self.ts * (self.vy[-1] * self.C[-1] * math.pow(0.5, math.pow(2.0, self.vx[-1]) + math.pow(2.0, self.vy[-1]))/ (1000 * self.m)))
            self.x.append(self.x[-1] + self.vx[-1] * self.ts)
            self.y.append(self.y[-1] + self.vy[-1] * self.ts)
    def show_results(self):
        font = {'family': 'serif',
                'color':  'green',
                'weight': 'normal',
                'size': 16,}
        pl.plot(self.x, self.y)
        pl.title('Trajectory of cannon shell', fontdict = font)
        pl.xlabel('x (km)')
        pl.ylabel('y (km)')
        pl.ylim(0, 30)
        pl.xlim(0, 65)
i=0
while i<4:
    a = cannon_shell(gravity_acceleration = g, mass = m,\
    time_step = ts, initial_x_position = xi,\
    initial_y_position = yi, initial_x_velocity = vxi * math.cos((math.pi/180) * 5 * i) - vyi * math.sin((math.pi/180) * 5 * i),\
    initial_y_velocity = vxi * math.sin((math.pi/180) * 5 * i) + vyi * math.cos((math.pi/180) * 5 * i), drag_coefficient = C, 
    sea_level_temperature = T_0)
    a.trajectory()
    a.show_results() 
    i=i+1
pl.show()
