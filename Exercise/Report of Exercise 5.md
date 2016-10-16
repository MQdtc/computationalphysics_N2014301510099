***Above all， I'm really sorry that I cannot finnish all the three problem I chose, because I spend too much time on the second one. Next time I will try my best to complete my exercises before the deadline.***
# **Report of Exercise 5**
  *Name: 马士全*  
    *Student Number: 2014301510099*  
    *物基二班*
    *Data: *<img src="http://latex.codecogs.com/gif.latex?Oct.14^{th}" alt="" title="" />
# Abstract
*In this Report, I will show some codes which are used to slove some realistic projection motions. Along with the book and professor Cai's [teaching plan](https://www.evernote.com/shard/s140/sh/26f85380-ee6c-4b4b-b33f-6871804d91ff/fb8cc702cb0e8ed7fafb50b2de4596ca), I will show you:*
> * Linear motion with air resistance---problem 2.5;
> * Two-dimensional projectile motion with air resistance---Problem 2.9;
> * Projectile motion with air drag, wind, or spin---Problem2.27 **(Not finish)**.

# Main Body
**First:**
Problem 2.5 expects us to simulate a low speed bicycle, and different from the simulation in our book, when a bicycle is at low velocity, it is more realistic to assume that the rider is able to exert a constant force. 
**Because of this assumptions, we can set the initial velocity as zero now.**
And we have to modify the motion equation of the bicycle:
<img src="http://latex.codecogs.com/gif.latex?\frac{dv}{dt}=\frac{F_0}{m}" alt="" title="" />
<img src="http://latex.codecogs.com/gif.latex?v_{i+1}=v_{i}+\frac{F_0}{m}\Delta{t}" alt="" title="" />
***And modify the calculate plate of the codes:***
This part of codes shows that there two kinds of different air drag, and they are distinguish with each other by the velocity of bicycle.
```python
def motion(self):
        _time = 0
        while(_time < self.tt):
            if self.v[-1] < 7 :
                self.v.append(self.v[-1] + self.ts * (self.f - self.C_1 * self.v[-1])/ self.m)
            else :
                self.v.append(self.v[-1] + self.ts * (self.f - self.C_2 * (self.v[-1])*(self.v[-1]))/ self.m)
            self.t.append(_time)
            _time += self.ts
``` 
***Of course you can input the initial condition as you like:***
```python
    f = input("Please type the force:")
    m = input("Please type the mass:")
    ts = input("Please type the time step:")
    tt = input("Please type the total time:")
    vi = input("Please type the initial velocity:")
    C_1 = input("Please type the drag cofficient 1:")
    C_2 = input("Please type the drag cofficient 2:")
```
Here is the whole codes:
## [codes for small velocity bicycle](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Codes/small%20velocity%20bicycle.py)
```python
"""
Created on Sat Oct 15 16:53:43 2016
@author: MQdtc
"""
import pylab as pl
class small_velocity_bicycle:
    f = input("Please type the force:")
    m = input("Please type the mass:")
    ts = input("Please type the time step:")
    tt = input("Please type the total time:")
    vi = input("Please type the initial velocity:")
    C_1 = input("Please type the drag cofficient 1:")
    C_2 = input("Please type the drag cofficient 2:")
    def __init__(self, force = f, mass = m, time_step = ts, total_time = tt, initial_velocity = vi, drag_coefficient_1 = C_1, drag_coefficient_2 = C_2):
    #At low velocity it is more realistic to assume that the rider is able to exert a constant force        
        self.v = [initial_velocity]
        self.t = [0]
        self.m = mass
        self.f = force
        self.ts = time_step
        self.tt = total_time
        self.C_1 = drag_coefficient_1
        self.C_2 = drag_coefficient_2
    def motion(self):
        _time = 0
        while(_time < self.tt):
            if self.v[-1] < 7 :
                self.v.append(self.v[-1] + self.ts * (self.f - self.C_1 * self.v[-1])/ self.m)
            else :
                self.v.append(self.v[-1] + self.ts * (self.f - self.C_2 * (self.v[-1])*(self.v[-1]))/ self.m)
            self.t.append(_time)
            _time += self.ts
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,}
        pl.plot(self.t, self.v)
        pl.title('small velocity bicycle with air resistance', fontdict = font)
        pl.xlabel('time ($s$)')
        pl.ylabel('velocity')
        pl.text(0.2 * self.tt, 0.9 * self.v[-1], 'velocity with time', fontdict = font)
        pl.show()
a = small_velocity_bicycle()
a.motion()
a.show_results()  
```
## resluts 
Here is The results:
![smb](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Pictures/small%20velocity%20bicycle.PNG)

**Second:**
***Problem 2.9*** ask us to calculate the trajectory of cannon shell including both air drag and the reduced air density at high altitudes.
We have to modif the motion equtions of cannon shell:
$$\rho=\rho_0(1-\frac{ay}{T_0})^{\alpha}$$
$$x_{i+1}=$$

**[Here is the codes](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Codes/cannon%20shell.py)**

```python
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
```
**Results**
![cs1](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Pictures/cannon%20shell%201.PNG)
![cs2](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Pictures/cannon%20shell%202.PNG)
# References and Thanks
[teaching plan of Chapter 2](https://www.evernote.com/shard/s140/sh/26f85380-ee6c-4b4b-b33f-6871804d91ff/fb8cc702cb0e8ed7fafb50b2de4596ca)
*卢超同学的一些建议*
