class Rectangle:
   def __init__(self,l,w):
       self.length = l
       self.width = w

   def area(self):  # function, returns and doesn't change the state
       return self.length * self.width

   def perimeter(self):  # function
       return 2 * self.length + 2 * self.width

   def scaleSize(self,scale):  # procedure, changes the state, not returning
       self.length = self.length * scale
       self.width = self.width * scale
   
   def display(self): # accessor, it prints.
       print('Length:',self.length, 'Width:', self.length, 'Area:', self.area(), 'Perimeter:',self.perimeter())
    
if __name__ == "__main__":
    Long = Rectangle(10,5)
    Wide = Rectangle(14,10)
    Long.display()
    Wide.display()
