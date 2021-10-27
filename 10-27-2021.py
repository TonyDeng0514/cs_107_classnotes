import queue107

def cowl(q) -> list:
  assert type(q) == type(queue)
  a = [0*q.len()]
  for i in range(q.len()):
    a[q.len()-i] = q.front().__str__
    q.dequeue(i)
  return a
  
