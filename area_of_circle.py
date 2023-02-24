# programm to calculate area of a circle
radius=float(input("enter radius: "))
def area_of_circle(radius, pi=3.14):
    area=radius*radius*pi
    return area
print(area_of_circle(radius, pi))