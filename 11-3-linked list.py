class Node:
   def __init__(self, x = None):
      self.val = x
      self.next = None

      
class linkedlistADT:
    def __init__(self, head = None, rest = None):
        if head == None: # empty constructor
            self.rep = None
        else:           # extending constructor
            assert type(rest) == linkedlistADT
            temp = Node(head)
            temp.next = rest.rep
            self.rep = temp

    def empty(self):
        return self.rep == None

    def head(self):
        return self.rep.val

    def rest(self):
        assert not self.empty()
        temp = linkedlistADT()
        temp.rep = self.rep.next
        return temp

	# insert what at position where starting at 0
    def insert(self, what, where):
        pass

    def remove(self, x):  # mutate list to remove x if there; 1st found
        pass
