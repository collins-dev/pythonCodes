# election in east africa
east_african_nation=["kenya","uganda","tanzania"]
nationality=input("Enter your nationality: ").lower()
age=int(input("enter your age: "))

if age>=18 and nationality in east_african_nation:
    print("allowed to vote")
else:
    print("not allowed to vote ")