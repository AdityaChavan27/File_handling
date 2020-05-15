
# coding: utf-8

# In[6]:


#1.	Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
l1=[1,2,3,4,5,6.7,7+8j,"Aditya","Riyaz","Yashika"]
print(l1)
print(type(l1[0]))
print(type(l1[6]))
print(type(l1[7]))
print(type(l1[5]))


# In[7]:


#2. 	Create a list of size 5 and execute the slicing structure
l1=[1,2,3,4,5]
print(l1[:])
print(l1[2:])
print(l1[:4])
print(l1[1:5:2]) # Slicing with step size


# In[18]:


"""
3. 	Create a list of given structure and run 
	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list [1, 2, 3, 4]
Access list [600,  700]
Access list [100, 300, 500, 600, 800]
Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list [10]
Access list [ ]
"""
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][0:4])
print(x[6:8])
print(x[0::2])
print(x[::-1])
print(x[5][5][0])
print(list())


# In[22]:


"""
4. 	Create a list of thousand number using range and xrange and see the difference between each other.
"""
x=range(1000)
print(x)
y=xrange(1000)
print(y)


# In[23]:


#creating list using Range
z=[]
for i in range(1001):
    z.append(i)
print(z)


# In[ ]:


"""
5. Advantage of tuples over list

"""

1)
Python tuples are immutable
2)
Iterations are faster in tuple due to their immutable property.
3)
Whenever we want to keep our data secured,then we use tuples as the data inside the tuple cannot be changed.


# In[25]:


"""
6. 	Write a program in Python to iterate through the list of 
numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.
"""
for i in range(1,100):
    if(i%3==0):
        print(i)
    elif(i%2==0):
        print(i)

        


# In[47]:


"""
7. 	Write a program in Python to reverse a string and 
print only the vowel alphabet if exist in the string with their index.
"""
user_inp=input("Enter the string : ")
z=user_inp[::-1].lower()
for i in range(len(z)):
    if(z[i]=="a" or z[i]=="e" or z[i]=="i" or z[i]=="o" or z[i]=="u"):
       print(z[i] ,":" ,i)
    else:
        pass
    


# In[50]:


# With no user_input
n="Consultadd"
z=n[::-1].lower()
for i in range(len(z)):
    if(z[i]=="a" or z[i]=="e" or z[i]=="i" or z[i]=="o" or z[i]=="u"):
       print(z[i] ,":" ,i)
    else:
        pass
    


# In[51]:


"""
8. 	Write a program in Python to iterate through the 
string “hello my name is abcde” 
and print the string which has even length of word.
"""
string="hello my name is abcde"
for i in range(len(string)):
    if(i%2==0):
        print(string[i])


# In[56]:


#Removing spaces
string="hello my name is abcde"
for i in range(len(string)):
    if(i%2==0) and (string[i].isalpha()):
        print(string[i])


# In[70]:


"""
9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
"""
#Using List
x=[1,2,3,4,5,6,7,8,9,-1]
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)):
        if(x[i]+x[j]==8):
            print(x[i],x[j])


# In[81]:


"""
10. 	Write a program in Python to complete the following task:
Create two different list as in even_list and odd_list
Ask user to enter the number in the range of 1,50 and make sure 
if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
Keep that in mind you can only add 5 items in each list
Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

"""
even_list=[]
odd_list=[]
counter=0
count_even=0
count_odd=0
while(counter!=10):
    user_inp=int(input("Enter the number in the range of 1-50 : "))

    if(user_inp %2 ==0):
        if(count_even<5):
            even_list.append(user_inp)
            count_even+=1
        else:
            print("You can only enter 5 even values")
            continue
    else:
        if(count_odd<5):
            odd_list.append(user_inp)
            count_odd+=1
        else:
            print("You can only enter 5 odd elements")
            continue
    counter=counter+1
print("Even_List : ",even_list)
print("Sum of Even_list : ",sum(even_list))
print("Max of Even_list : " , max(even_list))
print("Odd_List : ",odd_list)
print("Sum of odd_list : ",sum(odd_list))
print("Max of odd_list : " ,max(odd_list))


# In[84]:


"""
Write a program to find out the occurrence of a specific word from an alphanumeric statement.
Example: 12abcbacbaba344ab  
Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
"""
n="12abcbacbaba344ab"
d=dict()
for i in n:
    if(i.isalpha()):
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    else:
        continue
print(d)



# In[96]:


"""
12.Generate and print another tuple whose values are even numbers
in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""
a=(1,2,3,4,5,6,7,8,9,10)
b=tuple()
for i in a:
    if(i%2==0):
        b=b+ (i,)
print(b)

