import nose
from binarySearch import binary_search

VALUES = [1,3,4,4,5,7,9,10]

def test_first():
    assert binary_search(1, VALUES) == 0

def test_duplicate():
    assert binary_search(4, VALUES) == 2

def test_middle():
    assert binary_search(5, VALUES) == 4
    
def test_last():
    assert binary_search(10, VALUES) == 7

def test_missing_start():
    assert binary_search(-3, VALUES) == -1
    
if __name__ == '__main__':
    nose.runmodule()