#prgramm to calculate the compound interest
principal=float(input("Enter principalin ksh: "))
rate=float(input("Enter rate in percentage: "))
time=float(input("Enter time in months: "))
def compund_interest(principal,rate,time):
    compoundInterest= principal * (pow((1 + rate / 100), time))
    return compoundInterest
print("Your compound interest is ksh",compund_interest(principal,rate,time))