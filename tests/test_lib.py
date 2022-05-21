# tests/test_lib.py

import numpy as np
from mlproject.lib import hello_world, try_me

def test_length_of_hello_world():
    '''
    This function tests, if the length of the input string is unequal zero
    '''
    assert len(hello_world()) != 0
    
def test_try_me():
    '''
    This function tests, if for a=1, b=1, c=2_000 two imaginary roots are returned
    '''
    assert np.shape(try_me(a=1, b=1, c=2_000))[0] == 6