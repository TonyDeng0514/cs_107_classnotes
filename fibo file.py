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
