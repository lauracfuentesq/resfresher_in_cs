from get_neighbors import get_neighbors
import numpy as np

x = np.loadtxt('data/synth_train.txt')

def test_can_we_do_something():
    # Test case 1: Check if the number of neighbors returned is equal to 3
    assert len(get_neighbors(x, x[0], 3)) == 3

    # Test case 2: Check if the number of neighbors returned is equal to 5
    assert len(get_neighbors(x, x[1], 5)) == 5

    # Test case 3: Check if the number of neighbors returned is equal to 0
    assert len(get_neighbors(x, x[2], 0)) == 0

    # Test case 4: Check if the number of neighbors returned is equal to the total number of data points
    assert len(get_neighbors(x, x[3], x.shape[0])) == x.shape[0]
