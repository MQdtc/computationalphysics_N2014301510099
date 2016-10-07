import pylab as pl
import numpy as np
class uranium_decay_A_and_B:
    N_A = input("Input Initial number of nuclei_A :")
    N_B = input("Input Initial number of nuclei_B :")
    tc = input("Input time constant :")
    tod = input("input time of duration :")
    ts = input("Input time step :")
    def __init__(self, number_of_nuclei_A = N_A, number_of_nuclei_B = N_B, time_constant = tc, time_of_duration = tod, time_step = ts):
        # unit of time is second
        self.n_uranium_A = [number_of_nuclei_A]
        self.n_uranium_B = [number_of_nuclei_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nuclei_A ->", number_of_nuclei_A)
        print("Initial number of nuclei_B ->", number_of_nuclei_B)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.n_uranium_A[i] + ((self.n_uranium_B[i] + self.n_uranium_A[i]) / self.tau - 2 * self.n_uranium_A[i] / self.tau )* self.dt
            tmp_B = self.n_uranium_B[i] + ((self.n_uranium_A[i] + self.n_uranium_B[i]) / self.tau - 2 * self.n_uranium_B[i] / self.tau )* self.dt
            self.n_uranium_A.append(tmp_A)
            self.n_uranium_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt) 
    def show_results(self):
        self.et_A = []
        self.et_B = []
        for j in range(len(self.t)):
            temp_A = (self.n_uranium_A[0] + self.n_uranium_B[0])/2 + 0.5 * (self.n_uranium_A[0] - self.n_uranium_B[0]) * np.exp(-2 * self.t[j] / self.tau)
            temp_B = (self.n_uranium_A[0] + self.n_uranium_B[0])/2 + 0.5 * (self.n_uranium_B[0] - self.n_uranium_A[0]) * np.exp(-2 * self.t[j] / self.tau)
            self.et_A.append(temp_A)
            self.et_B.append(temp_B)
        pl.plot(self.t, self.et_A, 'b', label = "theoretical A")
        pl.plot(self.t, self.et_B, 'r', label = "theoretical B")
        pl.plot(self.t, self.n_uranium_A, 'b+', label = "$N_A$")
        pl.plot(self.t, self.n_uranium_B, 'r+', label = "$N_B$")
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0, self.time)
        pl.legend()
        pl.show()
a = uranium_decay_A_and_B()
a.calculate()
a.show_results()
