import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#simple 3d function to minimize
#converts single input array to 3 variables
#simple function who's minimum is the origin (0,0,0)
def func(i):
    a = i[0]
    b = i[1]
    c = i[2]
    return(a**2+b**2+c**2)

#running scipy minimize function with initial nonzero guess
#starting point
start = [2,2,2]

result = minimize(func,start)
x = result.x[0]
y = result.x[1]
z = result.x[2]
value = func([x,y,z])

print('Location of minimum:',x,y,z)
print('Minimum value of function:',value)

