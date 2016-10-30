# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:01:35 2016

@author: MQdtc
"""
import math
import matplotlib.pyplot as plt
#加入宏包
#设置初值条件
class pendulum:
    def __init__(self, FD, theta1, theta2, omega1, omega2, T, damping = 0.5, \
    length = 9.8, gravity = 9.8, driveOmega = 0.666666667, timestep = 0.04):
        self.l = length
        self.q = damping
        self.g = gravity
        self.Omega = driveOmega
        self.dt = timestep
        self.omega1 = [omega1]
        self.omega2 = [omega2]
        self.theta1 = [theta1]
        self.theta2 = [theta2]
        self.theta = [theta2 - theta1]
        self.drive = FD
        self.t = [0]
        self.T = T
        return None
    #利用数值法计算对应的角速度和角度
    def calculate_normal(self):
        while (self.t[-1] < self.T):
            omega1 = self.omega1[-1] - ((self.g/self.l) * math.sin(self.theta1[-1]) + self.q * self.omega1[-1]\
            - self.drive * math.sin(self.Omega * self.t[-1])) * self.dt
            self.omega1.append(omega1)
            theta1 = self.theta1[-1] + self.omega1[-1] * self.dt
          #  if theta1 <= -math.pi:
          #      theta1 = theta1 + 2 * math.pi
          #  elif theta1 >= math.pi:
          #      theta1 = theta1 - 2 * math.pi
          #  else:
          #      pass
            self.theta1.append(theta1)
            omega2 = self.omega2[-1] - ((self.g/self.l) * math.sin(self.theta2[-1]) + self.q * self.omega2[-1]\
            - self.drive * math.sin(self.Omega * self.t[-1])) * self.dt
            self.omega2.append(omega2)
            theta2 = self.theta2[-1] + self.omega2[-1] * self.dt
          #  if theta2 <= -math.pi:
          #      theta2 = theta2 + 2 * math.pi
          #  elif theta2 >= math.pi:
          #      theta2 = theta2 - 2 * math.pi
          #  else:
          #      pass
            self.theta2.append(theta2)
            t = self.t[-1] + self.dt
            self.t.append(t)
            theta = abs(self.theta2[-1] - self.theta1[-1])
            self.theta.append(theta)
A1 = pendulum(FD = 1.2, omega1 = 0, omega2 = 0, theta1 = 0.2, theta2 = 0.201, T = 160)
A1.calculate_normal()
plt.semilogy(A1.t, A1.theta, "blue")
plt.show()
