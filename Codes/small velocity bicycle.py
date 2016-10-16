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
            if self.v[-1] < 14 :
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
