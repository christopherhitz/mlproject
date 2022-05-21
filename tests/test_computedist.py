# tests/test_lib.py

from mlproject.distance import haversine 
def test_distance():
    '''
    This function tests, if the calculated distance is greater or equal zero
    '''
    assert haversine() != 0