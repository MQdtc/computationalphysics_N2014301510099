# Abstract
-------
*Use the drawing function of Matplotlib insde the Python and the numerical approach to learn the decay process of radioactive particles. And in this report, I will focus on a hypothetical investigation of the equilibrium state of radioactivity.* 
# Background
--------
After learning the decay process of $U$, we can 

# Main body
---------
From the [*teaching paln*](https://www.evernote.com/shard/s140/sh/d351f9a3-8076-4274-944b-7043e0ce8cf3/4f89e8630604ea23262f00b3ed11f8ad), we can know that the The radioactive decay process satisfies the equation：  
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_{nuclear}}{dt}=-\frac{N_{nuclear}}{\tau}" alt="" title="" />  
where the $N_{nuclear}$ is the **number of the nuclear**, <img src="http://latex.codecogs.com/gif.latex?\tau" alt="" title="" /> is the **time constant** for the decay.  
It's easy to get the solution:    
<img src="http://latex.codecogs.com/gif.latex?N_{nuclear}=N_{nuclear}(0)e^{-t/\tau}" alt="" title="" />  
In order to learn the process in a numerical apporach, we can make a *Taylor expansion* to <img src="http://latex.codecogs.com/gif.latex?N_{nuclear(t)}" alt="" title="" /> :   
<img src="http://latex.codecogs.com/gif.latex?N_{nuclear}(t)=N_{nuclear}(0)+\frac{dN_{nuclerar}}{dt}t+\frac{1}{2}\frac{d^2N_{nuclear}}{dt^2}t^2" alt="" title="" />
Omitting high order terms：
<img src="http://latex.codecogs.com/gif.latex?N_{nuclear}(t)=N_{nuclear}(0)+\frac{dN_{nuclear}}{dt}t" alt="" title="" />  
use the **Euler method** :    
<img src="http://latex.codecogs.com/gif.latex?N_{nuclear}(t+\Delta t)=N_{nuclear}(t)-\frac{N_{nuclear}(t)}{\tau}\Delta t" alt="" title="" />  
According to the problem $1.5$, we have :  
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_A}{dt}=\frac{N_B}{\tau}-\frac{N_A}{\tau}" alt="" title="" />  
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_B}{dt}=\frac{N_A}{\tau}-\frac{N_B}{\tau}" alt="" title="" />   
so we have the numeber of expressions of $A$ and $B$：  
<img src="http://latex.codecogs.com/gif.latex?N_A(t+\Delta t)=N_A(t)+[\frac{N_B}{\tau}-\frac{N_A}{\tau}]\Delta t" alt="" title="" />     
<img src="http://latex.codecogs.com/gif.latex?N_B(t+\Delta t)=N_B(t)+[\frac{N_A}{\tau}-\frac{N_B}{\tau}]\Delta t" alt="" title="" />  
Now I can start designing my program


 **Codes**
 ------
[The main codes of Exercise 4:](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Codes/Exercise%204%20main.py)  
 ```python
 import pylab as pl
class uranium_decay_A_and_B:
    N_A = input("Input Initial number of nuclei_A ->")
    N_B = input("Input Initial number of nuclei_B ->")
    tc = input("Input time constant ->")
    tod = input("input time of duration ->")
    ts = input("Input time step ->")
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
            tmp_A = self.n_uranium_A[i] + (self.n_uranium_B[i] / self.tau -self.n_uranium_A[i] / self.tau )* self.dt
            tmp_B = self.n_uranium_B[i] + (self.n_uranium_A[i] / self.tau -self.n_uranium_B[i] / self.tau )* self.dt
            self.n_uranium_A.append(tmp_A)
            self.n_uranium_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.n_uranium_A)
        pl.plot(self.t, self.n_uranium_B)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei A and B')
        pl.show()
a = uranium_decay_A_and_B()
a.calculate()
a.show_results()
 ```

----------
**Result**
------



# References and Thanks
------
[How to think like a computer scientist – Learning with Python: Interactive Edition 2.0](http://interactivepython.org/runestone/static/thinkcspy/index.html)



