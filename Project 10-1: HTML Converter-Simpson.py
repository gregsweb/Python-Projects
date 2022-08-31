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



Now we 

We use sub() method to replace the tags with "".

Now we remove empty elements in the list using loop.

Now the list contains the desired data which is obtained after the removal of tags and spaces.

We print the data in the list in the desired format.

Note:

Make sure that the indentation is followed correctly when you try the code.

Store the html file and code file in the same location i.e., under same folder.

