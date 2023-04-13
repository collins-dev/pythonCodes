# class to calulate the area and perimeter of a rectange
length=float(input("Enter the length in meters: "))
width=float(input("Enter the width in meters: "))
class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
    
R = Rectangle(length, width)
print("the are of the rectacle is: ", R.area(), "cubic meters")
print("the peimeter of the rectangle is: ", R.perimeter(),"cubic meters")