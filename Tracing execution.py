'''

>>> assert gezinto(4, 12) == 3
>>> assert gezinto(4, 17) == 4
>>> assert gezinto(3, 17) == 5
>>> assert gezinto(2, 17) == 8
>>> assert gezinto(3.7, 16.2) == 4
>>> assert gezinto(12, 4) == 0

# >>> assert gezinto(-5, -21) 

>>> assert gezinto(5, 0) == 0

# the recursion limit is usually 1000.
>>> assert gezinto(3, 9237) == 3079

#>>> assert gezinto(10, 9237) == 

#>>> assert gezinto(-3, -2) 

'''
import sys
sys.setrecursionlimit(5000)

def gezinto(d, n):
    if d > n:
        return 0
    else:
        return 1 + gezinto(d, n-d)


def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
