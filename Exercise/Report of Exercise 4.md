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
where the $N_{nuclear}$ is the **number of the nuclear**, <img src="http://latex.codecogs.com/gif.latex?tau is the **time constant** for the decay.  
It's easy to get the solution:  
<img src="http://latex.codecogs.com/gif.latex?N_{nuclear}=N_{nuclear}(0)e^{-t/\tau}
In order to learn the process in a numerical apporach, we can make a *Taylor expansion* to <img src="http://latex.codecogs.com/gif.latex?N_{nuclear(t)} : 
<img src="http://latex.codecogs.com/gif.latex?N_{nuclear}(t)=N_{nuclear}(0)+\frac{dN_{nuclerar}}{dt}t+\frac{1}{2}\frac{d^2N_{nuclear}}{dt^2}t^2



 **Codes**
 ------


----------
**Result**
------



# References and Thanks
------
[How to think like a computer scientist – Learning with Python: Interactive Edition 2.0](http://interactivepython.org/runestone/static/thinkcspy/index.html)



