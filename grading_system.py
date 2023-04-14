#program to generate an avarage grade
unit1=float(input("Enter the unit1 marks: "))
unit2=float(input("Enter the unit2 marks: "))
unit3=float(input("Enter the unit3 marks: "))
unit4=float(input("Enter the unit4 marks: "))
unit5=float(input("Enter the unit5 marks: "))
unit6=float(input("Enter the unit6 marks: "))
mean_score=(unit1+unit2+unit3+unit4+unit5+unit6)/6
if(mean_score<=39):
    print("your mean score is:", mean_score, "You have a fail")
elif(mean_score>=40 and mean_score<=49):
    print("your mean score is:", mean_score, "You have a D")
elif(mean_score>=50 and mean_score<=59):
    print("your mean score is:",mean_score, "You have a C")
elif(mean_score>=60 and mean_score<=69):
    print("your mean score is:", mean_score, "You have a B")
else:
    print("your mean score is:", mean_score, "You have an A")
    