# class to calulate the area and perimeter of a rectange
length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
    
R = Rectangle(length, width)
print(R.area())
print(R.perimeter())