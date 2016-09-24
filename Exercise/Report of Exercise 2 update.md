# This is the Report of the Exercise 2 update
----------
**brief introduction:**
-------------
Professer Cai said that we can try to complete our seconde homework use "dictonary", not just use the basic fuction "print" in his last class. So I studied some features of "dictionary", and refer some codes of my senior students to make my codes better.

 ***The new codes:***
 ----------
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
    qwhitespace = ['        ', '        ', '        ', '        ', '        ', '        ', '        ']  
    alphabet = {'whitespace':qwhitespace, 'a':qA, 'b':qB, 'c':qC, 'd':qD, 'e':qE, 'f':qF, 'g':qG, 'h':qH, 'i':qI, 'j':qJ, 'k':qK, 'l':qL, 'm':qM, 'n':qN, 'o':qO, 'p':qP, 'q':qQ, 'r':qR, 's':qS, 't':qT, 'u':qU, 'v':qV, 'w':qW, 'x':qX, 'y':qY, 'z':qZ}  
    screen = [' ']*7      
    for j in range(7):  
        for i in range(lens):  
            screen[j] = screen[j] + alphabet[name[i]][j]   #get your name use "#"  
        print (screen[j])      
    return screen   
    
def main():  
    name = input('please input your English name:')    # python 3+ have removed fuction raw_input  
    lens = len(name)  
    name = name.lower()    # exchange what you input into lower case letters  
    kunnoname(name,lens)  

main()  

**Results:**  
![Result of Exercise 2 update](https://github.com/MQdtc/computationalphysics_N2014301510099/blob/master/Pictures/Exercise%202%20update.PNG)

**Reference and Thanks**
---------
[ chenfeng2013301020145 homework_code Exercise03](https://github.com/chenfeng2013301020145/computational-physics_N2013301020145/blob/master/Exercise/Homework_1%262.py)

