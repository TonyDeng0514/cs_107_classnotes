#What would be the output of this code ?
x = 100
print("1. Global x:", x)
class Test():
    x = x + 100 # x is local and class variable
    y = 300
    def __init__(self):
        self.x = 500 # instance variable i.e. belongs to object
        print("2. Global x:", x)
        print("3. Class x:", Test.x)
        print("4. Object x:", self.x)
        try:
            #print(y)  # Trying to access y which is not defined
            print(self.y) # self.y is accessible
        except NameError as e:
            print("5.", e)  
            
# Driver code
Object = Test()

