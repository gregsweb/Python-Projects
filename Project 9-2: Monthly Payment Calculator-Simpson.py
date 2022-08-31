#!/usr/bin/env python3
#IS 296 Unit 3: File I/O, Exceptions, Numbers 
#Gregory Simpson 
#IS 296 Python Programming 
#Herzing University Atlanta  
#July 2022 
#Dr. J. Cardenas 
#Project 9-2: Monthly Payment Calculator-Simpson



def monthlyPayment(loan_amount, rate, years):
    n = years * 12
r = (rate / 100) / 12
MonPay = (r * loan_amount * ((1+r) ** n)) / (((1+r) ** n) - 1)
return MonPay

choice=""
while choice != "n":
    loan_amount = int(input('Loan Amount: '))
rate = float(input('Yearly Interest rate : '))
years = int(input('Years :'))

print()
print("Loan amount: ",loan_amount)
print("Yearly interest rate: ",rate,"%")
print("Years: ",years)
print('Monthly payment: {:.1f}'.format(monthlyPayment(loan_amount, rate,
years)))
print()
choice= input("Continue? (y/n):")
