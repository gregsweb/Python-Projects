#!/usr/bin/env python3
#IS 296 Unit 3: File I/O, Exceptions, Numbers 
#Gregory Simpson 
#IS 296 Python Programming 
#Herzing University Atlanta  
#July 2022 
#Dr. J. Cardenas 
#Project 9-3:Sales Report-Simpson

#define the sales list of lists for 4 regions
sales = [[1540.0, 2010.0, 2450.0, 1845.0], [1130.0, 1168.0, 1847.0, 1491.0], [1580.0, 2305.0, 2710.0, 1284.0], [1105.0, 4102.0, 2391.0, 1576.0]]
print('Sales Report')
print('%10s%10s%10s%10s%10s'%('Region','Q1','Q2','Q3','Q4'))

# loop to print the each quarter sales for each region
for i in range(len(sales)):
print('%10d' %(i+1)),

for j in range(len(sales[i])):
print('{0:10,.2f}'.format(sales[i][j])),
print()

print('Sales by region:')

# loop to print the total sales by region
for i in range(len(sales)):
    total_sales = 0
print('Region %d : '%(i+1))

for j in range(len(sales[i])):
    total_sales = total_sales + sales[i][j]

print('{:,.2f}'.format(total_sales))

print('Sales by quarter:')

quarter_sales = [0]*len(sales[0])

# calculate the quarterly sales

for i in range(len(sales)):

for j in range(len(sales[i])):

quarter_sales[j] = quarter_sales[j] + sales[i][j]

# display quarter sales

for i in range(len(quarter_sales)):

print('Q%-5d : %s' %(i+1,'{0:10,.2f}'.format(quarter_sales[i])))

total_sales = 0

# calculate total sales of all regions in all quarters

for sale in quarter_sales:

total_sales = total_sales + sale

# display the annual sales

print('Total annual sales, all regions: $%s' %('{0:10,.2f}'.format(total_sales)))

