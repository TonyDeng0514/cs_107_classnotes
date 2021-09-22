'''
N = 7
fibonacciSeries = [0,1]
if N>2:
    for i in range(2, N):
        nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]    
        fibonacciSeries.append(nextElement)

print(fibonacciSeries)


def fib(n: int)->int:
    assert n >= 0
    answer = 1
    prev = 1
    prev2 = 1
    for i in range(n-1):
        prev2 = prev
        prev = answer
        answer = prev + prev2
    return answer
'''

def fib(n: int)->int:
    
    def fib_helper(n:int, answer:int, prev:int, prev2:int, i:int)-> int:
        if i >= n:
            return answer
        else:
            return fib_helper(n, prev+answer, answer, prev, i+1)
        
    
    assert n >= 0

    return fib_helper(n, 1, 1, 1, 1)

print(fib(7))
