"""
circle of words list

>>> q = queue107()
>>> q.enqueue('b')
>>> q.enqueue('a')
>>> q.enqueue('c')
>>> print(q)
['b', 'a', 'c']
>>> cowl(q)
['b', 'a', 'c']
['a', 'c', 'b']
['c', 'b', 'a']

"""



from queue107 import *

def cowl(q) -> list:
  assert type(q) == type(queue107())
  if q == q.empty():
    print(q)
  else:
    for i in range(q.len()):
      print(q)
      q.enqueue(q.front())
      q.dequeue()
  
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")