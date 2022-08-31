#!/usr/bin/env python3
#IS 296 Unit 2 Assignment-Function, Module, List, Tuple
#Gregory Simpson 
#IS 296 Python Programming 
#Herzing University Atlanta  
#July 25, 2022 
#Dr. J. Cardenas 
#Project 5-1: Debug Tax Calculator
#See Project 4-4:Tax Calculator
#See sales_tax


TAX = 0.06

def sales_tax(total)
    sales_tax = total * tax
    return total

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)
    
if __name__ == "__main__":
    main()

