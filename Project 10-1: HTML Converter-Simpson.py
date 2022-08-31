#Project 10-1: HTML Converter-Simpson




#importing re module for regular expressions
import re 
print("HTML Converter")
print()
print("File name: ",end=" ")

#To print the name in bold format if needed.
print('\033[1m' + 'groceries.html' + '\033[0m')
print()


#1.Open the file
#The file is opened using open() method. 
f=open("groceries.html",'r')


#2.Read the data from the file into data variable
#The data is read into data variable.
data=f.readlines()

#create list to store the file data in it.
l=[] 
for i in data:
    l.append(i.strip()) 

for i in range(len(l)):

#3.Use sub() to replace the tags with "".
#remove the tags using regular expressions methods.
l[i]=re.sub("^<..>","",l[i]) 
l[i]=re.sub("</..>$","",l[i])


#After removal of tags, remove the empty elements from list
count=l.count('') 
for i in range(count):
l.remove('')


#6.Print the data in desired format.
print(l[0]) 
for i in l[1:]:
#5
print("*",end=" ")
print(i)
Explanation:





