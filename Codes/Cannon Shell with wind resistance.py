# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:01:20 2016

@author: MQdtc
"""
# An update version for my cannon shell programm
import math
import matplotlib.pyplot as plt
import numpy.random as ran
# 加入所需要的包
g = 9.8
B2_divide_m = 0.00004
y_zero = 10000
a = 0.0065
T_0 = 293
alpha=2.5
# 设定常数参量
class cannon:
   # 定义一个最基础的 cannon shell 的类
    # initialize variables    
    def __init__(self, v_0, v_wind, launch_angle, yFinal=0):
        self.x_0 = 0
        self.y_0 = 0
        self.yload = yFinal
        self.v_0 = v_0
        self.Angle = launch_angle
        self.angle = launch_angle*math.pi/180
        self.v_x0 = self.v_0*math.cos(self.angle)
        self.v_y0 = self.v_0*math.sin(self.angle)
        self.v_wind = v_wind
        self.dt = 0.01
        return None
    # 定义其他非重力的阻力，这里只是给出一个抽象的力的函数        
    def resistance_F(self, v_x, v_y, y=1):
        return 0,0
    # 计算加农炮的飞行轨迹
    def trajactory(self):
        self.X = [self.x_0]
        self.Y = [self.y_0]
        self.V_x = [self.v_x0]
        self.V_y = [self.v_y0]
        self.T = [0]
        while not (self.Y[-1] < self.yload and self.V_y[-1] < 0):
            V_x = self.V_x[-1] + self.resistance_F(v_x = self.V_x[-1], v_y = self.V_y[-1], y = self.Y[-1])[0]*self.dt
            V_y = self.V_y[-1] - g*self.dt + self.resistance_F(self.V_x[-1], self.V_y[-1])[1]*self.dt
            self.V_x.append(V_x)
            self.V_y.append(V_y)
            meanV_x = 0.5*(self.V_x[-1] + self.V_x[-2])
            meanV_y = 0.5*(self.V_y[-1] + self.V_y[-2])
#            meanV=math.sqrt(meanVx**2+meanVy**2) # not used in Cannon0 because there is no air drag
            X = self.X[-1] + meanV_x*self.dt
            Y = self.Y[-1] + meanV_y*self.dt
            self.X.append(X)
            self.Y.append(Y)
        # 修正数值法在坐标上带来的误差        
#        r=-self.Y[-2]/self.Y[-1]
        self.X[-1] = ((self.Y[-2] - self.yload)*self.X[-1] + (self.yload - self.Y[-1])*self.X[-2])/(self.Y[-2] - self.Y[-1])
        self.Y[-1] = self.yload
        return 0
    # 由于有可能会在计算中射过头（x坐标）因为x坐标没有加判断语句，上面这个操作是为了修正最后落地点的x坐标
    def distance(self):
        return self.X[-1]
    def height(self):
        return max(self.Y)
        # 获得最终的落地坐标以及最大高度
    # 画出飞行轨迹
    def plot(self, color):
        plt.plot(self.X, self.Y, color, label = "$%dm/s$,$%d\degree$, no air drag"%(self.v_0, self.Angle))
        return 0
class cannon_air(cannon):
    #定义理想的加农炮
    #先定义我们需要的额外的阻力项       
    def resistance_F(self, v_x, v_y, y=1):
        vl = math.sqrt(v_x**2+v_y**2)
        self.F_x = -B2_divide_m*v_x*vl
        self.F_y = -B2_divide_m*v_y*vl
        return self.F_x, self.F_y
    def plot(self, color):
        plt.plot(self.X, self.Y, color, label = "$%dm/s$,$%d\degree$, uniform air drag"%(self.v_0, self.Angle))
        return 0      
class cannon_air_altitude_wind(cannon):
    #定义我们需要的含有海拔空气阻力以及风力影响的加农炮
    #先定义额外的阻力项
    def resistance_F(self, v_x, v_y, y=1):
        self.F_x = - B2_divide_m*math.sqrt((v_x - self.v_wind)**2 + v_y**2)*(v_x - self.v_wind)*(1 - a*y/T_0)**alpha
        self.F_y = - B2_divide_m*math.sqrt((v_x - self.v_wind)**2 + v_y**2)*v_y*(1 - a*y/T_0)**alpha
        return self.F_x, self.F_y  
    def plot(self, color):
        plt.plot(self.X, self.Y, color, label="$%dm/s$,$%d\degree$, wind risistance"%(self.v_0, self.Angle))
        return 0
class newcannon:
    #定义一个初值满足均匀分布的加农炮模型
    def __init__(self, v_0, v_wind, launch_angle, yFinal=0):
        self.x_0 = 0
        self.y_0 = 0
        self.yload=yFinal
        self.v_0 = ran.uniform(0.95*v_0, 1.05*v_0)
        self.Angle = ran.uniform(launch_angle - 2, launch_angle + 2)
        self.angle = self.Angle*math.pi/180
        self.v_x0 = self.v_0*math.cos(self.angle)
        self.v_y0 = self.v_0*math.sin(self.angle)
        self.v_wind = ran.uniform(0.9*v_wind, 1.1*v_wind)
        self.dt=0.01
        return None
class newcannon_air_altitude_wind(newcannon):
    #定义我们需要的含有海拔空气阻力以及风力影响的加农炮
    #先定义额外的阻力项
    def resistance_F(self, v_x, v_y, y=1):
        self.F_x = - B2_divide_m*math.sqrt((v_x - self.v_wind)**2 + v_y**2)*(v_x - self.v_wind)*(1 - a*y/T_0)**alpha
        self.F_y = - B2_divide_m*math.sqrt((v_x - self.v_wind)**2 + v_y**2)*v_y*(1 - a*y/T_0)**alpha
        return self.F_x, self.F_y   
#筛选炮弹的最远落点的组合
Distance=[]
for i in range(90):
    A = cannon_air_altitude_wind(v_0 = 700, v_wind = -10, launch_angle = i)
    A.trajactory()
    newDistance = A.distance()
    Distance.append(newDistance)
maxDistance = max(Distance)
maxAngle = Distance.index(maxDistance)
B1 = cannon_air_altitude_wind(v_0 = 700, v_wind = -10, launch_angle = maxAngle)
B2 = cannon_air_altitude_wind(v_0 = 700, v_wind = 0, launch_angle = maxAngle)
def result1():
    B1.trajactory() 
    B2.trajactory()  
    plt.plot(B1.X, B1.Y, 'b-', label="v of wind = -10")
    plt.plot(B2.X, B2.Y, 'r--', label="v of wind = 0")
    plt.title('the longest distance of a cannon shell with wind resistance') 
    plt.legend(loc="upper right") 
    plt.xlabel("Distance [m]")
    plt.ylabel("Hieght [m]") 
    plt.show() 
result1()
print("%dm"%(B1.distance()))
print("%dm"%(B2.distance()))
