"""
queue107: an implementation of a queue represented as a Python list

>>> que = queue107()
>>> assert que.empty()
>>> que.enqueue("chi")
>>> que.enqueue("rho")
>>> que.enqueue("tau")
>>> assert not que.empty()
>>> assert que.front() == "chi"
>>> que.dequeue()
>>> assert que.front() == "rho"

"""

class queue107:
    def __init__(self):
        self.rep = []

    def empty(self):        # returns True iff the queue is empty
        return self.rep == []

    def front(self):        # returns the value at the front of the queue
        return self.rep[0]

    def enqueue(self, x):   # mutates the queue to add x at the back
        self.rep.append(x)

    def dequeue(self):      # mutates the queue to remove x from the front
        self.rep.pop(0)

    def __str__(self):      # abstraction to text
        return str(self.rep)

    def len(self):
        return len(self.rep)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
