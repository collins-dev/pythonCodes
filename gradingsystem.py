#Grading system programm
mark1=float(input("Please enter your mark1: "))
mark2=float(input("please enter your mark2: "))
def grading_system(mark1,mark2):
    avarage=(mark1+mark2)/2
    if avarage >= 0 and avarage <= 39:
        print("Grade E")
    elif avarage >= 40 and avarage <=49:
        print("Grade D")
    elif avarage >= 50 and avarage <=59:
        print("Grade c")
    elif avarage >= 60 and avarage <= 69:
        print("Grade B")
    else:
        print("Grade A")
    return avarage
print("Your total marks is:",grading_system(mark1,mark2))