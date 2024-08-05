from src.Theories.Python_practices import *

def test_increment():
    assert increment(3) == 4

def test_sort_function():
    name = input()
    assert sort_function(name)