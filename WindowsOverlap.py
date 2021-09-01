"""
INSERT TEST SUITE HERE

>>> windowOverlap( 116 ,  258 ,  86 ,  163 ,  228 ,  313 ,  141 ,  206 )

"""

from Logic import *

def windowOverlap(xmin1: float, xmax1: float, ymin1: float, ymax1: float, xmin2: float, xmax2: float, ymin2: float, ymax2: float) -> bool:
    precondition(xmin1 <= xmax1 and xmin2 <= xmax2 and ymin1 <= ymax1 and ymin2 <= ymax2)
    """postcondition: return true iff there exists x such that min1 <= x <= max1 and min2 <= x <= max2 """
    return False # FIX

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
