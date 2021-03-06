'''

>>> assert gezinto(4, 12) == 3
>>> assert gezinto(4, 17) == 4
>>> assert gezinto(3, 17) == 5
>>> assert gezinto(2, 17) == 8
>>> assert gezinto(3.7, 16.2) == 4
>>> assert gezinto(12, 4) == 0

# >>> assert gezinto(-5, -21) 

>>> assert gezinto(5, 0) == 0
>>> assert gezinto(3, 9237) == 3079

#>>> assert gezinto(-3, -2) 

'''

from Logic import *


def gezinto(d, n):
    precondition(d > 0 and n >= 0)
    count = 0
    while n >= d:
        n -= d
        count += 1
    postcondition(type(count) == type(1))
    return count

def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
