# programm to calculate area of a circle
radius=float(input("enter radius in meters: "))
pi=22/7
def area_of_circle(radius):
    area=radius*radius*pi
    return area
print(area_of_circle(radius))