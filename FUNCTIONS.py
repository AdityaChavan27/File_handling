
# coding: utf-8

# In[ ]:


"""
1. 	Write a program to reverse a string.
Sample data: “1234abcd”
Expected Output: “dcba4321”
"""
sample_data="1234abcd"
res=sample_data[::-1]
print(res)


# In[ ]:


"""
2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
Expected Output:
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""

def identify_upper_or_lower(n):
    count_upper=0
    count_lower=0
    for i in n:
        if(i.isupper()):
            count_upper+=1
        elif(i.islower()):
            count_lower+=1
    print("No. of Upper case characters :",count_upper) 
    print("No. of lower case characters :",count_lower)
identify_upper_or_lower("ConsultADD")
            


# In[ ]:


"""
3.Create a function that takes a list and returns a new list with unique elements of the first list.
"""
def unique(n):
    return list(set(n))
n=[1,2,1,1,3,"Aditya","Aditya"]
unique(n)


# In[ ]:


"""
Write a program that accepts a hyphen-separated sequence of words 
as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
"""
def hyper_sep_seq(n):
    z=n.split("-")
    z.sort()
    k="-".join(z)
    return k
n="i-am-a-good-boy"
hyper_sep_seq(n)


# In[ ]:


"""
5.Write a program that accepts a sequence of lines as input and 
prints the lines after making all characters in the sentence capitalized.
Sample input:
Hello world
Practice makes perfect
Expected Output:
HELLO WORLD
PRACTICE MAKES PERFECT
"""
n=input("Enter the lines : ")
print(n.upper())


# In[ ]:


"""
6.Define a function that can receive two integral numbers 
in string form and compute their sum and print it in console.
"""
def num(a,b):
    a=int(a)
    b=int(b)
    sum_a=a+b
    return sum_a
a='13'
b='23'
num(a,b)


# In[ ]:


"""
7.Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line.
"""

def max_str(a,b):
    if(len(a)>len(b)):
        return a
    elif(len(a)<len(b)):
        return b
    else:
        return print(a,"\n",b)
a="asdscds"
b="xsxsdfd"
max_str(a,b)


# In[ ]:


"""8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
"""
var=tuple(map(lambda x:x**2,range(1,21)))
print(var)


# In[ ]:


def square():
    a=tuple()
    for i in range(1,21):
        a=a+(i**2,)
    return print(a)
square()
        


# In[ ]:


"""
9.Write a function called showNumbers that takes a parameter called limit. 
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
Example: If the limit is 3 , it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD
"""
def showNumbers(limit):
    for i in range(0,limit+1):
        if(i%2==0):
            print( i ,"EVEN")
        else:
            print( i ,"ODD")
        
limit=15
showNumbers(limit)


# In[ ]:


"""
10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
"""
var=list(filter(lambda x:x%2==0,range(1,21)))
print(var)


# In[ ]:


"""11. 	Write a program which can map() and filter()
to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
Hints: Use map() to generate a list.
     	     Use filter() to filter elements of a list
            Use lambda to define anonymous functions
"""

var=list(map(lambda x:x**2,filter(lambda x:x%2==0,range(1,11))))
var


# In[3]:


"""
12.Write a function to compute 5/0 and use try/except to catch the exceptions
"""
def divide_by_zero(a,b):
    while(True):
        try:
            c=a/b
            print(c)
            break
        except ZeroDivisionError:
            print("Please provide other number than zero to complete the operation")
            break
        finally:
a=5
b=0
divide_by_zero(a,b)


# In[36]:


"""
Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
Goal : Turn [1,2,3,4,5,6,7] to 1234567 
"""
from functools import reduce
import operator
l1=[[1,2,3],[4,5],[6,7,8]]
red=reduce(operator.add,l1)
a=red[0:7]
for i in a:
    print(i,end="")


# In[39]:


"""
 14. 	What is the output of the following codes:
 """
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)


# In[42]:


def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()

