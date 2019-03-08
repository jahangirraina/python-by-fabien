#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Python Programming: Essentials 1
# 
# #### Variables are used to store values. 
# 
# #### A string is a series of characters, surrounded by single or double quotes. 

# Hello world

# In[1]:


print("Hello World") # print() is your first function


# Hello world via a variable

# In[2]:


message= "i am in london" # assigning a string to a variable

print(message) # message is a variable


# 
# 
# Concatenation (combining strings) 

# In[3]:


first_name = 'jahangir' 
last_name = 'raina' 

full_name = first_name + ' ' + last_name 

print(full_name)


# In[4]:


full_name


# In[5]:


# little funny one: multiply words! 
print(full_name * 5)


# In[6]:


print(first_name , last_name ) # the comma adds a space automatically


# 
# 
# ## List
# 
# A list stores a series of items in a particular order. 
# 
# You access items using an index, or within a loop. 
# Make a list 

# In[7]:


bicycles = ['mountain', 'road', 'race', 'penny-farthing']

print(bicycles)

hill = 'mountain'
bikes = [hill, 'road', 'race', 'penny-farthing']


# In[8]:


print(bikes)


# In[ ]:


addon = ['raleigh' , 'brompton']

bicycles = bicycles + addon # add a list to a list

print(bicycles)


# In[13]:


bicycles = bicycles + ['peugeot']


# In[14]:


print(bicycles)


# Get the first item in the list

# In[15]:


first_bike = bicycles[0]  # list[position]
print (first_bike)


# In[16]:


third_bike = bicycles[2]  # list[position]
print (third_bike,first_bike)


# Get the last item in the list

# In[17]:


last_bike = bicycles[-1]
print(last_bike)


# In[18]:


# write code to print the penultimate (i.e. one before last) bike
second_last = bicycles[-2]


# In[19]:


print(second_last)


# # Working with Strings
# 
# ## split() function

# In[20]:


# the function split() cuts a string at specified character position then store the result in a list

sentence = "'Jeff Bezos divorce: Amazon billionaire 'dating married former TV presenter'"

words = sentence.split(' ')

print(words)


# In[21]:


url = 'https://www.standard.co.uk/news/politics/brexit-secretary-dominic-raab-quits-his-post-a3990626.html'

elements = url.split('/')
print(elements)


# In[ ]:





# In[27]:


# adapt to get the first and second part from an email address

email = "trainingsupport@pairview.co.uk"

########## your code below#############

parts = email.split('@')
print(parts[0],parts[1])

#alternative
first = email.split('@')[0]
second = email.split('@')[1]


# In[25]:


# write code to get the first name and the last name from the full name that 
# can include 1 or many middle names

################your code################
myname = "Elizabeth Alexandra Mary Windsor"

x=myname.split(' ')
y=x[0]+' '+x[-1]
print(y)


# ## join() function

# In[ ]:


words


# In[26]:


# the function join() take a list of strings and concatenate its elements separated by the character passed to it
separator =' '

sentence = separator.join(words)

print(sentence)


# ## strip() function

# In[30]:


# the function strip() removes unwanted characters (spaces usually) 
# at the beginning and ending of a string
stri = "0000000@@   this is a polluted # string example   @@0000000"

x= stri.strip('0').strip('@').strip()
print(x)

# strip() is equivalent to strip(' ')


# ## replace(old_word,new_word) function

# In[32]:


# and now I present you the function replace
clean =x.replace('polluted # ','cleaned ')
print(clean)


# # for in statement
# ### Looping through a list 

# In[33]:


bicycles = ['mountain', 'road', 'race', 'penny-farthing']


for n in bicycles: 
    print(n)
    print('Still in the loop')
 
print('this is outside the loop')


# In[ ]:


bicycles = ['mountain', 'road', 'race', 'penny-farthing']

c=1
word =bicycles[0]
print(c,' : ',word)
c=c+1

word =bicycles[1]
print(c,' : ',word)
c=c+1

word =bicycles[2]
print(c,' : ',word)
c=c+1

word =bicycles[3]
print(c,' : ',word)
c=c+1

print('this is outside the loop')


# ## range () function
#     

# In[34]:


# loop above equivalent to 

for i in range(0,4): #for i = 0 to 3 do in C++
    c = i + 1
    print(c ,' : ',bicycles[i])
    


# In[ ]:


# range function testers


# In[35]:


for number in range(8): # one only attribute = range(0,8)
    print(number)


# In[36]:


for number in range(2,8): # first is start , second the one before
    print(number)


# In[37]:


for number in range(2,8,2): # first is start , second the one before the last # 3rd the step
    print(number)


# ## Adding items to a list

# In[38]:


# add another string
bicycles.append('peugeot')
print(bicycles)


# In[ ]:


# equivalent to 
bicycles = bicycles  +  ['peugeot']


# In[39]:


# aside: insert
bicycles.insert(2,'BMX')
print(bicycles)


# In[40]:


# add a number!
bicycles.append(22)
print(bicycles)


# In[41]:


bicycles.remove('BMX') #removes the 1st instance in the list of the attribute
print(bicycles)


# In[ ]:





# In[42]:


bicycles.pop() # removes the last item in the list
print(bicycles)


# In[43]:


bicycles.pop(1) #will remove item at index 1
print(bicycles)


# In[44]:


# add a list!!
bicycles.append(['derailleur','shimano']) 
print(bicycles)

#YOU CAN ADD ANYTHING!!!


# In[45]:


# Code for accessing the second item in the list inside the list
print(bicycles[-1][0])


# In[46]:


print(bicycles[-2][0])


# ## Making numerical lists

# In[47]:


# initialisation 
cubes = [] 

# loop
for number in range(1, 7): 
    cubes.append(number**3) 

print(cubes)

# ** operator is power


# In[53]:


# write code to calculate the average of numbers from 5 to 15
# the average is the sum divided by the number of elements

series = [5,6,7,8,9,10,11,12,13,14,15]
#range(5,16)

sum=0
freq=0


for x in range(5,16):
    sum=sum+x
    freq=freq+1
    
ave=sum/freq  
print(ave)


# In[54]:


series = [5,6,7,8,9,10,11,12,13,14,15]
#range(5,16) fabien solution

total=0
count=0

for n in series:
    total = total + n
    count = count + 1
    
result = total/count
print(result)


# ## len() function

# In[ ]:


# the amazing Len function - aka the length of everything
#len()    
   
l = len (range(5,16)) # number of elements in the numerical series
print(l)

print( len (bicycles)) #number of items in list

print(len('guardian')) # number of character


# # List comprehensions : Advanced
# 

# In[55]:


cubes = [x**3 for x in range(1, 7)] 
print(cubes)
# equivalent to 


# In[ ]:


cubes = [] 
for x in range(1, 7): 
    cubes.append(x**3) 
print(cubes)


# ## List comprehension exercise 
# 
# Write one line of Python that takes this list and makes a new list that has only the even elements of this list in it.

# In[ ]:


List = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ## Slicing a list 

# In[56]:


finishers = ['Sue','Elliot', 'Kumiko','Damien','Aaron'] 
first_two = finishers[:2] # all up to 2 but not 2
print(first_two)


# In[57]:


last_two = finishers[2:] # from 2 (included) up to end
print(last_two)


# In[58]:


f = finishers[:2] + finishers[2:]
print(f)


# In[59]:


last_two = finishers[-3:]
print(last_two)


# ### Tuples
# 
# Tuples are similar to lists, but the items in a tuple can't be modified. 

# Making a tuple 

# In[60]:


# tuple of numbers
dimensions = (1920, 1080)

# tuples of tuples
pushbikes= ('mountain', 'road', 'race', 'penny-farthing')

#tuple of different types of variables
hold_all = (35, 'Data Science', [1,2,3,4,5], (1,7))

print(hold_all)


# In[61]:


t, x, y , z= hold_all 
print(x)


# In[62]:


#hold_all[0]= 34

print(hold_all[0])


# ### If statements are used to test for particular conditions and respond appropriately.
# 
# # if (condition) : action

# In[63]:


# If statement
age = 25
commonwealth = True

if age >= 18: 
    print("You may be able to vote")
    print("something else")


# In[64]:


if (age >= 18 and commonwealth == True): # or xor
    print("You can vote!") 
 


# In[65]:


#If-elif-else statements 
if age < 4: 
    price = 0
    print('Kids go free')
elif age < 18: price = 10 
elif age > 65: price = 12
else: price = 15
    

print(price)


# Conditions
# 
# tests equals
# x == 42 
# 
# not equal 
# x != 42  
# 
# greater than 
# x > 42 
# 
# greater than or equal to
# x >= 42 
# 
# less than
# x < 42 
# 
# less than or equal to
# x <= 42

# In[66]:


x = 57 #  assign 57 to x

# (x<42) is  a test with a value of True of False
#print('is x smaller than 42?', x < 42)

Var = (x > 42 )

print(Var)

print(x<42)


    


# In[68]:


grade = 80

test = (grade> 70) # pass rate

if test :
    print("passed")
else :
    print("failed please retake")
    
if test :
    print("admission to uni")   


# ## Conditional test with lists 
# ## IN
# ## NOT IN

# In[74]:


print('race' in bicycles)
print(bicycles)


# In[70]:


print('downhill' not in bicycles)


# In[78]:


if 'downhill' not in bicycles:
    bicycles.append('downhill')
print(bicycles)


# In[80]:


# downhill tricycle
if 'downhill' not in bicycles or 'tricycle' not in bicycles :
    bicycles = bicycles + ['downhill','tricycle']


# In[84]:


bicycles.pop(-2)
print(bicycles)


# In[87]:


newbikes = ['downhill', 'tricycle', 'fixie']


# In[88]:


for b in bicycles:
    if b not in newbikes:
        newbikes.append(b)
    else: print(b,' already in')
        
print(newbikes)


# Assigning boolean values

# In[86]:


game_active = True
can_edit = False

if game_active or can_edit:
    print('yay')


# # Exercise
# 
# Take a list of numbers
# and write a program that prints out all the elements of the list that are less than 5.

# In[89]:


# set list

List = [1, 1, 25, 3, 55, 8, 13, 21, 3, 5, 89]
less = []
# your code below
for n in List:
    if n<5:
        less.append(n)
print(less)


# In[ ]:


# i want to put in a new list the odd numbers


# In[91]:


odds =[]
for y in List:
    if y%2==1:
        odds.append(y)
print(odds)


# In[90]:


#  modulo operation % gives the remainder of division
# div operation // that performs an integer division

print(5 % 2)
print(5 // 2)


# # Dictionaries 
# they store connections between pieces of information
# 
# Each item in a dictionary is a key-value pair

# Simple dictionaries {}

# In[93]:


word_frequency = {'Data' : 14, 'Science': 10, 'Machine': 5, 'Learning' : 8}


real_dictionary = {'a': 'string that defines a', 'abc': 'definition of abc'}


# with different value types
car = {'make' : 'Mazda', 'model' : '3 sport', 'engine_size_cc': 2259,
       'colour': 'laser blue', 'dimensions_mm' : {'w':1795 , 'l':4465 , 'h':1465}}


# Accessing a value

# In[94]:


print( car['colour'])
# dict[key] accesses the value in key , value pair


# In[95]:


#write code to retrieve the dictionary inside the dictionary
print( car['dimensions_mm'])


# In[96]:


# retrieve the value in the dictionary inside the dictionary
# width w
dict = {'w': 1795, 'l': 4465, 'h': 1465}
dict['w']

print( car['dimensions_mm']['w'])


# In[ ]:





# In[97]:


# Adding / modifying a new key-value pair
car['transmission_type'] = 'automatic'

car['colour'] = 'blood red'
# dic[key] = value
print(car)


# Values, Keys and Items

# In[98]:


print(car.items())


# In[99]:


print(car.keys())


# In[100]:


print(car.values())


# Looping through all keys

# In[101]:


# for keys in dictionary:

for k in car.keys(): 
    print(k + ' is a car characteristic') 


# Looping through all the values

# In[102]:


# write code to loop through all the values
for v in car.values(): 
    print(v, "is a characteristic") 


# Looping through all key-value pairs

# In[103]:


for k,v in car.items():
    print(k , 'is', v)


# In[105]:


Tuples_List = [(1,2,3) , (4,5,6) , (7,8,9)]

for a , b , c in Tuples_List:
    print(round(a*b/c,2))


# In[108]:


#Write a Python script to concatenate following dictionaries to create a new one. 

#Sample Dictionary : 
dic1={1:'Royal Dutch Shell', 2:'BP'} 
dic2={3:'Total', 4:'Volkswagen'} 
dic3={5:'Glencore Xstrata',6:'Gazprom'}


# In[113]:


final = dic1

for k,v in dic2.items():
    final[k]=v
    
for k,v in dic3.items():
    final[k]=v
    
print(final)


# In[114]:


# Write a Python script to check if a given key already exists in a dictionary.

test_number = 7
key_in_dictionary = False

### your code ####

if test_number in final.keys():
    print('got it already')
else: print('pls add to the dictionary')


# ### Programs can prompt the user for input. 
# All input is stored as a string. 
# 
# Prompting for a value

# In[115]:


# prompting for a value
name = input("What's your name? ") 
print("Hello, " + name + "!") 


# In[1]:


# prompting for a number

age = int(input("How old are you? ")) #return a string
print(age*7)


# In[4]:


pi = input("What's the value of pi? ") 
pi = round(float(pi),2)
print(pi)


# # Exercise
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# In[11]:


#initialisation
current_year = 2019

name = input("What's your name? ") 
age = int(input("What is your age?"))

print("Hello, " + name + " you will turn 100 in the year ", current_year+(100-age))


# In[ ]:


# Write a Python program that prompts for a month name and converts it to a number
# of days.
#List of months: January, February, March, April, May, June, July, August
#, September, October, November, December                                

# Example
#Input the name of Month: February                                       
#No. of days: 28/29 days 

month = input("Input the name of Month: ")


# In[ ]:




