def rangeOverlap(x0: float, x1: float, x2: float, x3: float) -> bool:
    assert x0 <= x1 and x2 <= x3
    
    # min1<=max2 and min2<=max1
    
    if (x1 >= x2 and  x3 >= x0):
        return True
    else:
        return False

assert rangeOverlap(0, 3, 6, 8) == False
assert rangeOverlap(0, 6, 3, 8) == True
