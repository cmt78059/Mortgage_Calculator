from mortgage import Loan
from decimal import *

print("Welcome to the Loan Calculator\n")
print("1.)Enter Your Loan Information")
print("2.)See a loan summary")
print("3.)See a summary of nth month")
print("4.)Enter extra payment information")

#Entering Loan Information
p=float(input("Enter the principal: $"))
i=float(input("Enter the interest rate: "))
t=int(input("Enter the term: "))
loan = Loan(principal=p, interest=i, term=t)

#Loan Summary
loan.summarize

#Loan Summary of nth Month
n=int(input("Enter the nth month: "))
loan.schedule(n)
print(loan.schedule(n))



#Loan Summary of nth Month



