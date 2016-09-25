# Abstract
-------
*This is the Report of Exercise 3, this Exercise is consisit of two levels. Level 1： make your name move horizontally on the screen; Level 2： Design a pattern and make it rotate on the screen* 
# Background
--------
Last time I use Python to show my English name on the screen, but you know, just show something isn't enough, sometimes we want to see a movable information.

# Main body
---------


 **Codes**
 ------
[Here is my codes for Level 1:](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Codes/Exercise%203%20L1.py)  

```python
import os
import time
qwhitespace = ['        ', '        ', '        ', '        ', '        ', '        ', '        ']
def kunnoname(name, lens):
    qA = ['   #    ', ' #   #  ', '#     # ', '# ### # ', '#     # ', '#     # ', '#     # ']
    qB = [' #####  ', '#     # ', '#     # ', '######  ', '#     # ', '#     # ', ' #####  ']
    qC = [' #####  ', '#     # ', '#       ', '#       ', '#       ', '#     # ', ' #####  ']
    qD = ['######  ', '#     # ', '#     # ', '#     # ', '#     # ', '#     # ', '######  ']
    qE = ['####### ', '#       ', '#       ', '######  ', '#       ', '#       ', '####### '] 
    qF = ['####### ', '#       ', '#       ', '#####   ', '#       ', '#       ', '#       ']
    qG = [' #####  ', '#       ', '#       ', '#   ### ', '#     # ', '#    ## ', ' #### # ']
    qH = ['#     # ', '#     # ', '#     # ', '####### ', '#     # ', '#     # ', '#     # ']
    qI = [' #####  ', '   #    ', '   #    ', '   #    ', '   #    ', '   #    ', ' #####  ']
    qJ = ['  ##### ', '     #  ', '     #  ', '     #  ', '     #  ', ' #   #  ', '  ###   ']
    qK = ['#     # ', '#    #  ', '#   #   ', '####    ', '#   #   ', '#    #  ', '#     # ']
    qL = [' #      ', ' #      ', ' #      ', ' #      ', ' #      ', ' #      ', ' #####  ']
    qM = ['#     # ', '##   ## ', '# # # # ', '#  #  # ', '#     # ', '#     # ', '#     # '] 
    qN = ['#     # ', '##    # ', '# #   # ', '#  #  # ', '#   # # ', '#    ## ', '#     # ']
    qO = [' #####  ', '#     # ', '#     # ', '#     # ', '#     # ', '#     # ', ' #####  '] 
    qP = ['######  ', '#     # ', '#     # ', '######  ', '#       ', '#       ', '#       ']
    qQ = [' #####  ', '#     # ', '#     # ', '#     # ', '#   # # ', '#    #  ', ' #### # '] 
    qR = ['######  ', '#     # ', '#     # ', '######  ', '#   #   ', '#    #  ', '#     # '] 
    qS = [' ###### ', '#       ', '#       ', ' #####  ', '      # ', '      # ', '######  ']
    qT = ['####### ', '   #    ', '   #    ', '   #    ', '   #    ', '   #    ', '   #    ']
    qU = ['#     # ', '#     # ', '#     # ', '#     # ', '#     # ', '#     # ', ' #####  ']
    qV = ['#     # ', '#     # ', '#     # ', ' #   #  ', ' #   #  ', '  # #   ', '   #    ']
    qW = ['#     # ', '#     # ', '#  #  # ', '#  #  # ', '#  #  # ', '# # # # ', ' #   #  ']
    qX = ['#     # ', ' #   #  ', '  # #   ', '   #    ', '  # #   ', ' #   #  ', '#     # ']
    qY = ['#     # ', '#     # ', ' #   #  ', '  # #   ', '   #    ', '   #    ', '   #    ']
    qZ = ['####### ', '     #  ', '    #   ', '   #    ', '  #     ', ' #      ', '####### ']
    alphabet = {'whitespace':qwhitespace, 'a':qA, 'b':qB, 'c':qC, 'd':qD, 'e':qE, 'f':qF, 'g':qG, 'h':qH, 'i':qI, 'j':qJ, 'k':qK, 'l':qL, 'm':qM, 'n':qN, 'o':qO, 'p':qP, 'q':qQ, 'r':qR, 's':qS, 't':qT, 'u':qU, 'v':qV, 'w':qW, 'x':qX, 'y':qY, 'z':qZ}
    screen = [' ']*7
    for x in range(4):    
        for j in range(7):
            for i in range(lens):
                screen[j] =qwhitespace[0]*x + screen[j] + alphabet[name[i]][j]   #get your name use "#"
            print screen[j]   
            screen = [' ']*7
        time.sleep(0.3)
        os.system('cls')
        print ('\n')*2*x
    return screen 
    
def main():
    name = raw_input('please input your English name:')   
    lens = len(name)
    name = name.lower()  # exchange what you input into lower case letters
    kunnoname(name,lens)
main()
 ```
 
[the codes for Level 2：](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Codes/Exercise%203%20L1%EF%BC%88trajectory%EF%BC%89.py)

----------
**Result**
------
Level 1:
------
Here is the result:  
![result of Exercise3 L1](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Pictures/Exercise%203%20L1%20move%20horizontally.gif)
(gif图片较大,流畅运行可能需要等待)  
if you want your name move horizontally, we can use these codes:  
 ```python
for x in range(4):    
        for j in range(7):
            for i in range(lens):
                screen[j] =qwhitespace[0]*x + screen[j] + alphabet[name[i]][j]   #get your name use "#"
            print screen[j]   
            screen = [' ']*7
        time.sleep(0.3)
        os.system('cls')
    return screen 
 ```
![result of Exercise3 L1](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Pictures/Exercise%203%20L1%20move%20sideling.gif)
(gif图片较大,流畅运行可能需要等待)  
If you want to your name move sideling, just need to change a litte codes:  
 ```python
    for x in range(4):    
        for j in range(7):
            for i in range(lens):
                screen[j] =qwhitespace[0]*x + screen[j] + alphabet[name[i]][j]   #get your name use "#"
            print screen[j]   
            screen = [' ']*7
        time.sleep(0.3)
        os.system('cls')
        print ('\n')*2*x
    return screen 
  ```
  Level 2:    
  ----
  What's more? We can even contorl the trajectory of the letters.  
  ![trajectory](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Pictures/Exercise%203%20L1%20move%20on%20a%20trajectory.gif)  
  [Here is the codes:](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Codes/Exercise%203%20L1%EF%BC%88trajectory%EF%BC%89.py)  
 ```python
 for x in range(20):    
        for j in range(7):
            for i in range(lens):
                screen[j] =' '*x*int(3+math.cos(x)*3) + screen[j] + alphabet[name[i]][j]   #get your name use "#"
            print screen[j]   
            screen = [' ']*7
        time.sleep(0.3)
        os.system('cls')
        print ('\n')*int(math.sin(x)*10)
    return screen 
 ```
  
  ---



# References and Thanks
------
[How to think like a computer scientist – Learning with Python: Interactive Edition 2.0](http://interactivepython.org/runestone/static/thinkcspy/index.html)



