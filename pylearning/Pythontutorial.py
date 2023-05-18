#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("hello world")


# # first notebook

# In[ ]:





# #variables in python

# In[17]:


x = 22

print(x)


# In[18]:


type(x)


# In[19]:


y = 'am good'


# In[20]:


type(y)


# In[21]:


x,y,z = 'vanilla', 'mint', 'hello'

print(x)
print(y)
print(z)


# # list

# In[22]:


ice_cream = ['chocolate','Vanilla', 'Rocky road']
x,y,z = ice_cream
print(x)
print(y)
print(z)


# In[24]:


# the best way to write a varioable
# 1 by using underscore infront or between the words

ice_cream = 'Vanilla'
_icecream = 'Vanilla'
_ice_cream = 'Vanilla'


#the wrong ways to write variables
# 1 beginning variables with numbers

_icecream = 'vanilla'


# # python data types

# In[25]:


#numeric data types
#1 integers = this are whole numbers both positive and negative

type(-12+44)


# In[26]:


#2 float = this are numerics that have decimal places 

type(10.5)
type(12+12.6)


# In[27]:


#3 complex = this are numerical data with letters in them that are like imaginary numbers
#  J is the only letter that is used in complex (if you use anyother letter you will get an error)

type(12+5j)


# In[28]:


# Boolean 
# this are only used to produce either a true or false results

type(True)
type(False)

#example use case

type(1 > 5)


# In[29]:


1 > 5


# In[30]:


# strings
# when assigning strings to a variable you should use Quatation marks

y = 'hae, eveyone'
type(y)


# In[31]:


#when using strings there are use of single quatation and double quatation which are used to do the same task

x = 'life is good'
x = "life is good"


# In[32]:


#triple quatations are used when you want to write a large amount of text like a poem or paragraph

multiline = """
The ice cream vanquished
my longing for sweets,
upon this diet i look away,
it no longer exists on this day
"""


# In[33]:


print(multiline)


# In[34]:


type(multiline)


# In[35]:


a= 'hello world'
print(a[:5])


# # list

# In[36]:


#list
#stores multuiple values list are stored in brackets[]
# list are positioned just as strings and a position 0 we have 1

[1,2,3,4,5]


# In[37]:


['BMW','Mercedes','Bently','Ferrari','Maybach']


# In[38]:


#to add a value to a list you use (.append) this adds to the furthest part

cars = ['BMW','Mercedes','Bently','Ferrari','Maybach']
cars.append('Buggati')
cars


# In[39]:


# to delete elements in a list you use (.pop)- this is used to remove a value by its index
#also the (remove) function can be used and in that you provide the value to be removed from the list

#(.pop)
numbers = [1,2,3,4,5,6,7,88,9]
numbers.pop(0)


# In[40]:


print(numbers)


# In[41]:


#(.remove)

bill = [99,87,65,44,33,23,54]
bill.remove(44)
print(bill)


# In[42]:


#changing things in a list
cars[0]= 'Tesla'
cars


# In[43]:


#nested list = this is a list within a list
nest_list = ['Vanilla',3,['Scoops','spoon'], True, 'Good']
nest_list[2]


# # tuple

# In[44]:


#tuples -can not be modified or changed after it has been created
#tuples are created using open parenthesis
#tuples are used when the data in them are not expected to change

good_day = (1,2,3,4,5,6)
type(good_day)


# In[45]:


for bum in good_day:
    print(bum)


# # set

# In[46]:


#sets
#values within a set cannot be accessed using index because its unordered

daily_stoic={1,2,3,4}
type(daily_stoic)


# In[47]:


#sets do not hold duplicate values
#used when one wants to avoid duplicates


daily_pint = {1,2,3}


# In[48]:


type(daily_pint)


# In[49]:


print(daily_pint)


# In[50]:


good_day = {1,2,3,5,7,8,77,2,3,7,4,5,6}  #you can see that during the print sets do not print duplicate values
print(good_day)


# In[51]:


#sets can be used to compare values between different sets

daily_log = {1,2,31,2,3,4,1,2,5,6,3,2}
wife_daily_log = {1,3,5,7,3,24,5,7,3,2,0}


# In[52]:


#when you want to find unique values from both daily_log and wife_daily_log

print(daily_log | wife_daily_log)


# In[53]:


#when you want to find value that are present in both daily_log and wife_daily_log

print(daily_log & wife_daily_log)


# In[54]:


#when you want to know the values that are not present in both daily_log and wife_daily_log

print(daily_log - wife_daily_log)


# # dictionaries

# In[55]:


#dictionaries
#has a key/value pair

dict_cream = {'name': 'Brian Michael', 'weekly intake': 5, 'favourite car':['Bently','Buggati','Mercedes']}


# In[56]:


type(dict_cream)


# In[57]:


print(dict_cream)


# In[58]:


dict_cream.values()


# In[59]:


dict_cream.keys()


# In[60]:


#dictionaries are called by the key

dict_cream['name']


# In[61]:


#you can also update the values within a dictionary

dict_cream['name'] = 'Bimax Motors'

print(dict_cream)


# In[62]:


#you can also update the whole dictionary the one we did before was on updating a single value

dict_cream.update({'name': 'Bimax Motors', 'production cost': 'five million', 'favourite car': ['Genim F12', 'Coldera01', 'Feyup']})

print(dict_cream)


# In[63]:


# to delete a value from the dictionary use del before the variable

del dict_cream['weekly intake']
print(dict_cream)


# # comparison,logical and membership operators in python

# In[64]:


#this contains mathematical operators

# equal to (==)

10 == 10


# In[65]:


#not equal to (!=)

10 != 40


# In[66]:


'Vanilla' == 'Vanilla'


# In[67]:


x = 'Brian'
y = 'Michael'

x != y


# In[68]:


# less than (<)

10 < 40


# # logical operators

# In[69]:


#logical operators often compined with logical operators

#And -----returns True if both statements are true
#Or ------Returns True if one of the statements is true
#Not -----Reverse the result, returns False if the statement is true


# In[70]:


(10 > 50) and (50 < 40)


# In[71]:


(70 > 30) and (10 < 30)


# In[72]:


(10 > 60) or (0.5 <20)


# In[73]:


not(50 > 10)


# # membership operators

# In[ ]:


#used to check if a value or string is within another value or sequence


#In -------Returns True if a sequence with the specified value is present in the object
#Not in -----Returns True if a sequence with the specified value is not present in the object


# In[74]:


brian_michael = 'i love cars soo much my guy'
'guy' in brian_michael #its like we are looking for the word guy in 'i love cars soo much my guy'


# In[75]:


'guy' in 'i love cars soo much my guy'


# In[76]:


_muranga = [1,2,3,34,4,4,5]

67 not in _muranga


# # If  -  Elif  -  Else  statements

# In[77]:


x = 25000000
if x == 25000000:
    print('am rich!')


# In[78]:


x = 25000000
if x > 25000000:
    print('am rich!')
else:
    print('work harder bro!')


# In[79]:


x = 25000000
if x > 25000000:
    print('am rich!')
elif x < 50000000:
    print('good job to me!')
else:
    print('work harder bro!')


# In[80]:


#onother way to write if else statement

print('it worked!') if 10 > 30 else print('it did not work ....')


# In[ ]:


#nested if statement


# # for loops

# In[ ]:


#used to do something repeatedly until untill a condition is met


# In[81]:


# Syntax  =  For var_name in sequence:                          for the var_name choose something meaningful
                #statement(s)

puke = ['jenny','Ram', 'Rahul', 'Pagal']


for names in puke:
    print(names)


# In[82]:


# for loops for dictonaries

dict_cream = {'name': 'Brian Michael', 'weekly intake': 5, 'favourite car':['Bently','Buggati','Mercedes']}


# In[83]:


for bull in dict_cream.values():    #to print values
    print(bull)


# In[84]:


for pig in dict_cream.keys():      #to print keys
    print(pig)


# In[85]:


for keys,value in dict_cream.items():   # to print out both keys and values
    print(keys,'->',value)


# In[86]:


#nested for loop


# In[87]:


flavors = ['Vanilla', 'Chocolate', 'Cookie Dough']
toppings = ['Hot Fudge', 'Oreos', 'Marshmallo']


# In[88]:


for one in flavors:
    for two in toppings:
        print(one, 'topped with', two)


# # while loops

# In[89]:


num = 0

while num < 5:
    print(num)
    num = num + 1


# In[90]:


# breaking while loop  --- you use break to break out of a loop even if the statement is true


num = 0

while num < 7:
    print(num)
    if num == 4:
        break
    num = num + 1


# In[91]:


#else statement in a while loop

num = 0
while num < 5:
    print(num)
    if num == 7:
        break
    num = num+1
else:
    print('no longer < 5')


# In[ ]:


# this will lead to a infinate loop

num = 0
while num < 5:
    print(num)
    if num == 3:
        continue
    num = num+1
else:
    print('no longer < 5')


# In[ ]:


# 3 won't be printed out

num = 0
while num < 5:
    num = num+1
    if num == 3:
        continue
    print(num)
else:
    print('no longer < 5')


# # functions

# In[ ]:


#they are only run when called
#example

def first_function():
    print('i finaly did it!')


# In[ ]:


#calling the function above
first_function()


# In[ ]:


#aguments in functions

def num_cool(number):
    print(number**2)


# In[ ]:


#calling the function

num_cool(6)   # 6 is the agument passed to the function


# In[ ]:


#passing more than one argument

def num_pass(number,power):
    print(number**power)


# In[ ]:


num_pass(5,2)


# In[ ]:


#abatury arguments   used when you are not sure about the number of arguments you want to pass

def num_arg(*number):
    print(number[0]*number[1])


# In[ ]:


num_arg(6,5,7,8,9)


# In[ ]:


#another example of how you can write the code above

tu_ple = (6,5,7,8,9)

def num_apt(*number):
    print(number[0]*number[1])


# In[ ]:


num_apt(*tu_ple)


# In[ ]:


#keyword Arguments   =  you define the values of the arguments

def num_one(power,number):
    print(number**power)


# In[ ]:


num_one(number = 3, power = 5)


# In[ ]:


#arbitary keyword argument
#in the arbitary argument we have one star here we are going to have two of them

def bri_an(**number):
    print('My number is: ' + number['brim'])


# In[ ]:


bri_an(brim = '356')


# In[ ]:


# when dealing with more than one

def muk_on(**arg):
    print('My number is: ' + arg['brim'] + ' My other number is: ' + arg['trim'])


# In[ ]:


muk_on(brim = '356', trim = '987')


# # converting data types

# In[ ]:


#converting integer and strings


# In[ ]:


num_int = 9
type(num_int)


# In[ ]:


num_str = '8'
type(num_str)


# In[ ]:


# when converting string to integer

str_con = int(num_str)


# In[ ]:


type(str_con)


# In[ ]:


#converting lists, sets and tuples


# In[ ]:


#converting list to tuple

list_type = [1,2,3,4,5,6]
type(list_type)


# In[ ]:


tuple(list_type)


# In[ ]:


type(tuple(list_type))


# In[ ]:


#converting a list into a set
#when converting a list into a set only the unique data will be selected because set eliminates duplicates

list_type = [1,2,3,4,3,4,2,3,9,78,5,4,5,2,1,0,4,6]
set(list_type)


# In[ ]:


type(set(list_type))


# In[ ]:


#converting dictionaries
dict_cream = {'name': 'Brian Michael', 'weekly intake': 5, 'favourite car':['Bently','Buggati','Mercedes']}
type(dict_cream)


# In[ ]:


dict_cream.items()


# In[ ]:


dict_cream.values()


# In[ ]:


dict_cream.keys()


# In[ ]:


#converting keys to a list
list(dict_cream.keys())


# In[ ]:


type(list(dict_cream.keys()))


# In[ ]:


#converting long strings into a list

puma = 'i love getting things done the right way'
list(puma)


# In[ ]:


type(list(puma))


# # BMI calculator (body mass index)

# #BMI Calculator reference
# https://mercer-health.com/services/weight-management-center/bmi-calculator#:~:text=Body%20Mass%20Index%2C%20or%20BMI,inches%20x%20height%20in%20inches

# In[ ]:


# BMI = (weight in kilogram) / (height in meters x height in meters)

#Under 18.5	Underweight	Minimal
#18.5 - 24.9	Normal Weight	Minimal
#25 - 29.9	Overweight	Increased
#30 - 34.9	Obese	High
#35 - 39.9	Severely Obese	Very High
#40 and over	Morbidly Obese	Extremely High

Name = input('Enter your Name: ')
weight = float(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in meters: '))
BMI = (weight) / (height**2)
print(BMI)


if BMI < 18.5:
    print(Name + ', You are underweight')
elif BMI <= 24.9:
    print(Name + ', You have a normal weight')
elif BMI <= 29.9:
    print(Name + ', You are overweight')
elif BMI <= 34.9:
    print(Name + ', You are Obese')
elif BMI <= 39.9:
    print(Name + ', You are Severly Obese')
else:
    print(Name + ', You are Morbidly Obese')


# # Automatic file sorter in File explorer

# In[ ]:


# the OS module       (that is what i should learn before doing this project)


# In[ ]:





# # Key data structrures for data science

# # string functions
# 
# # 1.lower and Upper

# In[ ]:


#used to change strings to lower case or upper case

scum = 'Everything you see around you'
scum.upper()


# In[ ]:


Town = 'WHERE THERE ARE MANY OPPOTUNITIES TO MAKE MONEY'
Town.lower()


# # 2. Strip

# In[ ]:


#used to get rid of white space and even new lines in a string

sing = '  everything is cool\n'
print(sing)


# In[ ]:


sing.strip()


# In[ ]:


#also used to get rid of other values within a string

make = '*****2345*****'
print(make)


# In[ ]:


make.strip('*')


# # 3. split

# In[ ]:


#used to return a list of words in a long string

lop = 'let us all play with the new guy'
lop.split(' ')


# # 4.string formatting
# 

# In[ ]:


#uses the format function   ---- used to add some words to a string

statement = 'we love {} {}'
statement.format('data','stealing')
print(statement.format('data','stealing'))


# # Numpy 

# ## numpy array

# In[ ]:


#numpy can be used to store a bunch of data in multidimensional array (1,2,3)
#numpy is used because it tends to be faster than using list


# ## application of Numpy
# 
# Mathematics(MATLAB Replacement), 
# Plotting (Matplotlib), 
# It is Backend of (Pandas, Connect 4, Digital Photography), 
# Machine Learning

# In[ ]:


import numpy as np


# ### Basics

# In[ ]:


#how to initialise an array

a = np.array([1,2,3])          # this is a one dimensional array
print(a)


# In[ ]:


b = np.array([[9.0,8.2,7.5,1.0],[5.3,8.0,9.0,1.2]])     # this is a two dimensional array of data type floats
print(b)


# In[ ]:


# how to get the dimension of your array
a.ndim


# In[ ]:


b.ndim


# In[ ]:


# to get the shape 
a.shape


# In[ ]:


b.shape     #(2,4) = says two rows and four columns


# In[ ]:


# to get type
b.dtype


# In[ ]:


# to get size
b.itemsize


# ## Accessing/ changing specific elements, rows, columns e.t.c

# In[ ]:


a = np.array([[8,6,5,3,8,9,1],[7,5,3,1,9,5,3]])
print(a)


# In[ ]:


a.shape


# In[ ]:


# geting a specific element  [row,column] (first row and column are 0)
# lets get 7

a[1,0]


# In[ ]:


# to get an entire row
a[0, :]


# In[ ]:


# to get a specific column
a[:, 4]


# In[ ]:


a[0, 1:6]


# In[ ]:


# changing elements (lets change 7 to 13)
a[1,0]=13
print(a)


# * 3D example

# In[ ]:


b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# In[ ]:


b.size


# In[ ]:


b.ndim


# In[ ]:


# getting specuific element

b[0,0,1]


# ## Initializing Different types of Arrays

# In[ ]:


# All zeros(0s) matrix  (return a new array of a given shape and type, filled with zeros)

np.zeros((2,3))


# In[ ]:


np.zeros((4,4,2))


# In[ ]:


# All ones(1s) matrix (returns a new array filled with 1s)

np.ones((2,3,4))


# In[ ]:


# Any other number matrix   (you specify the shape and also the values)

np.full((3,2,2), 22)     #(22 is the value to be filled that i have specified)


# In[ ]:


# Any other number (np.full_like)  (enables us to take a shape that has already been build)
a = np.array([[8,6,5,3,8,9,1],[7,5,3,1,9,5,3]])
a


# In[ ]:


np.full_like(a, 3)


# In[ ]:


#Random decimal numbers(random.rand)

np.random.rand(3,2)


# In[ ]:


#Random integer values(np.random.randint)
# 2 --- is the position argument

np.random.randint(9,size=(4,3))


# In[ ]:


#The identity matrix (its always a square so it requires one agument)

np.identity(4)


# In[ ]:


# Repeat a array (i have used in in a two dimensional array)

arr = np.array([[5,4,3,2]])
r1 = np.repeat(arr,3, axis=0)
print(r1)


# In[ ]:


arg = np.array([[5,6,7,8],[9,7,8,5]])
print(arg)


# In[ ]:


output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1]=9
print(z)
output[1:4,1:4] = z
print(output)


# ### when copying contents of another variable

# In[ ]:


# when you want to copy the contents of another variable you need to use the (.copy())
#the example below

a = np.array([1,2,3,4])
b = a
b[0] =1000
b
a


# In[ ]:


# when copying to use it diferrently

a = np.array([5,4,6,8])
b = a.copy()
b[0]= 100
b
a


# ## Mathematics using numpy

# In[ ]:


a = np.array([1,2,3,4])
a


# In[ ]:


#addition
# this adds it to all the values within the array

a+2


# In[ ]:


#subtraction(also subtracts everything from the array)

a - 4


# In[ ]:


#multiplication
a * 4


# In[ ]:


#division
a / 2


# In[ ]:


b = np.array([3,4,5,8])
a + b


# In[ ]:


np.sin(a)


# In[ ]:


np.cos(a)


# #### Numpy mathematical Documentation
# ####  For a lot more (https://docs.scipy.org/doc/numpy/reference/routines.math.html)

# In[ ]:





# In[ ]:


a = np .array([7,4,7,9,7,5])
a


# In[ ]:


a * 10


# In[ ]:


a


# In[ ]:


a += 10
a


# In[ ]:


a


# In[ ]:


a = np.arange(9)
a


# In[ ]:


a <= 3


# In[ ]:


a > 6


# In[ ]:


a.mean()


# ### Linear Algebra

# In[ ]:


# Linear Algebra is the one of the most important part in machine learning

a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

np.matmul(a,b)


# In[ ]:


### DO MORE ABOUT LINEAR ALGEBRA AND NUMPY THAT WILL ALSO BE USED IN MACHINE LEARNING


# ### Statistics

# In[ ]:


## Mean, mediun, Max, min

doo = np.array([[5,4,6,7],[8,7,9,6]])
doo


# In[ ]:


np.min(doo)


# In[ ]:


np.sum(doo)


# ## Reorganizing Arrays

# In[ ]:


# This is used to mainly change the shapes of arrays(Use the .reshape)

hell = np.array([[5,6,8,9,2],[7,9,4,6,2]])
print(hell)

hello = hell.reshape((5,2))
print(hello)


# In[ ]:


# Vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2])
np.vstack([v1,v2,v2,v1])


# In[ ]:


# horizontal stack

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

np.hstack((h1,h2))


# ## Miscellaneous
# ### Load Data from file

# In[ ]:


np.genfromcsv('Excel project')


# In[ ]:





# # Pandas

# In[3]:


import pandas as pd


# ### Importing Data into Jupyter notebook

# In[8]:


# To import data you have to give the route that the data is supossed to follow use the (pd.read_csv)(csv is a file name)

df = pd.read_csv('desktop/pandas/survey_results_public.csv')


# In[9]:


df


# In[10]:


# to get to know the number of column and rows in your data (use the .shape attribute)

df.shape


# ## Data types in pandas in our dataset
# #### Object means string
# #### Int64 is integer that stored in a 64 bit
# #### and float

# In[11]:


#To get more information about the data you are using use (.info())
#This gives you the columns and the data types that you are using

df.info()


# In[5]:


# To view all the columns in our dataset (.set_option('display.max_columns',_number of columns_))

df = pd.read_csv('desktop/pandas/survey_results_public.csv')
pd.set_option('display.max_columns', 79)
df


# In[4]:


# i want to put a schema file that we have that have matching questions to the dataset that we have
# so we will load in the schema file

schema_df = pd.read_csv('desktop/pandas/survey_results_schema.csv')
schema_df


# In[14]:


# to view all rows of your dataset(pd.set_option('display.max_rows'_number of rows_))

pd.set_option('display.max_rows', 79)
schema_df


# In[15]:


schema_df


# In[16]:


df


# In[6]:


schema_df


# In[9]:


# when you want to just see a certain amount of data(.head()) this for viewing the first 10 items

schema_df.head(10)


# In[10]:


#viewing the last 10(.tail())
df.tail()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




