#!/usr/bin/env python3
#IS 296 Unit 3: File I/O, Exceptions, Numbers 
#Gregory Simpson 
#IS 296 Python Programming 
#Herzing University Atlanta  
#July 2022 
#Dr. J. Cardenas 
#Project 7-3:Contact Manager-Simpson

import csv
try:
    with open(r'contacts.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            count+=1
except:
    print('File not found starting with creating a new file')
    with open(r'contacts.csv', mode='w',newline='') as csv_file:
        fieldnames = ['name', 'email', 'mobile']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'name': 'John Smith', 'email': 'Accounting', 'mobile': 'November'})
        writer.writerow({'name': 'Erica Meyers', 'email': 'IT', 'mobile': 'March'})

# starting taking Command from user
print('Command Menu \nlist-Display all contacts\nview- View a contact\nadd- Add a contact\ndel- Delete a contact\nexit- Exit program')
while True:
    a = input('\n\nCommand: ')
    if a=='exit':
        print('Bye!')
        exit()
    elif a=='list':
        with open(r'contacts.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            count=1
            for row in csv_reader:
                print(count,'. ',row[0])
                count+=1
    elif a=='view':
        no=input('\nNumber: ')
        try:
            no=int(no)
            if no<count:
                with open(r'contacts.csv', mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    counter=1
                    for row in csv_reader:
                        if counter==no:
                            print('Name',row[0])
                            print("Email: ",row[1])
                            print("Phone: ",row[2])
                        counter+=1
            else:
                print('Invalid Contact no')
        except:
            print('Invalid Integer')
    elif a=='add':
        name=input('Name: ')
        email=input('Email: ')
        phone=input('Phone: ')
        with open(r'contacts.csv', mode='a',newline='') as csv_file:
            fieldnames = ['name', 'email', 'mobile']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'name': name, 'email': email, 'mobile': phone})
            count+=1
    elif a=='del':
        delete_no=input('\nNumber: ')
        try:
            delete_no=int(delete_no)
            print(delete_no)
            if delete_no<count:
                
                with open(r'contacts.csv', mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    counter=1
                    full_list=[]
                    for row in csv_reader:
                        if counter!=delete_no:
                            full_list.append(row)
                        counter+=1
                with open(r'contacts.csv', mode='w',newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerows(full_list)
                    count-=1
                print('contact Deleted')
            else:
                print('Invalid Contact no')
        except:
            print('Invalid Integer')
    else:
        print('Please select a valid command from the Menu')
        





