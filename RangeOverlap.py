def rangeOverlap(x0: int, x1: int, x2: int, x3: int) -> bool:
    assert x0 <= x1 and x2 <= x3
    
    # min1<=max2 and min2<=max1
    
    if (x1 >= x2 and  x3 >= x0):
        return True
    else:
        return False

assert rangeOverlap(0, 3, 6, 8) == False
assert rangeOverlap(0, 6, 3, 8) == True
