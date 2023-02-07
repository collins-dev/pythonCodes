#program to calculate salary bonus
salary=float(input("Enter your salary: "))
period_of_service=float(input("Enter priod of service: "))
result1=0.1*salary
result2=0.08*salary
result3=0.05*salary
if(period_of_service>10):
   
    print("Your bonus is " ,result1)
elif(period_of_service>=6 and period_of_service<=10):
    
    print("Your bonus is ",result2)
else:
    print("Your bonus is ",result3)