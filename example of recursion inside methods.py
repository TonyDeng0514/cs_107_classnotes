class example:
    def __init__(self, n: int): # constructor
        self.rep = [0] * n # list init zeros
        self.size = n
        for i in range(len(self.rep)):
            self.rep[i] = i

    def reverse(self):     
        def rev_help(x: list)-> list: 
            if x == []:     # empty list
                return []
            else:
                head = x[0]
                rest = x[1:]
                return rev_help(rest) + [head]

        return rev_help(self.rep)

tester = example(5)
print(tester)       # what's wrong here?
print(tester.reverse())
