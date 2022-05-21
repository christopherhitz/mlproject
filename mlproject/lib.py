# lmproject/lib.py

import math


import math
import numpy as np
from cmath import sqrt


def hello_world(text="Hello world from mlproject"):
    '''
    This function prints a text
    Input:  text - Sring
    Output: text - String
    '''
    return text

def try_me(a=1, b=1, c=2_000):
    '''
    Check if a is zero. If yes, we can not go firther, since er can not divide by zero.
    '''
    if a == 0:
        print("Invalid")
        return -1
    '''
    Calcualte Discriminant (D)
    '''
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))
    '''
    Consider three cases for the Discriminant
    ''' 
    if d > 0: # If D>0 : Two real root exists.
        print("Roots are real and different.")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
        return (-b + sqrt_val) / (2 * a), (-b - sqrt_val) / (2 * a)
    elif d == 0: # If D=0 : Equal root exists
        print("Roots are real and same")
        print(-b / (2 * a)) 
        return -b / (2 * a)
    else: # d<0. If D<0 : Imaginary roots exists.
        print("Roots are real and imaginary")
        print(- b / (2 * a), ' + i', sqrt_val)
        print(- b / (2 * a), ' - i', sqrt_val)
        return  - b / (2 * a), ' + i ', sqrt_val, - b / (2 * a), ' - i ', sqrt_val 
    

if __name__ == "__main__":
    print(hello_world(text="Hi from lib.py and the function hello world"))
    print(hello_world())
    
    # try_me function
    print(try_me(a=1, b=1, c=2_000))