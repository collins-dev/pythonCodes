#programm to calculate the volume of a cylinder
height=float(input("enter height in meters: "))
radius=float(input("enter radiusin meters: "))
pi=3.142
area=radius*radius*pi
def volume_of_cylinder(area, height):
    volume=area*height
    return volume
print("volume of the cylinder is: ", volume_of_cylinder(area, height), "cubic meters")