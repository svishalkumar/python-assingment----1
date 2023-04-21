#!/usr/bin/env python
# coding: utf-8

# In[6]:


##exercise 1:Mailing Addresh


a="Name-vishal kumar"
b="Addresh-vill+po-puchhariya,ps-sangrampur,dis-east champaran,pin-845434,bihar"
n="Email-svishalkumar547@gmail.com"
print(a)
print(b)
print(n)


# In[7]:


##Exercise--2##


g=input("Enter your first Name\n ")
print("hello",g)


# In[ ]:





# Exercise--3

# In[1]:


##here we have used float function because we need float value##


lenth=float(input("enter the lenth of the room in meter = "))
width=float(input("Enter the width of the room in meter = "))
area=lenth*width
print(area,"Square meters")


# Exercise--4

# In[14]:


sqft_per_acre = 43560

lenth=float(input("enter the lenth of the room in feet : "))
width=float(input("Enter the width of the room feet : "))
area=(lenth*width) / sqft_per_acre
print(area)


# exercise----6
# 

# In[6]:


## This program will be compute the tax and  the tip for the meal.

## here Tax rate is given by me
# in python we use 4% as 0.04 & 18% as 0.18



Tax_rate=0.04
Tip_rate=0.18
cost=float(input("What is the cost of your meal ="))
tax=cost*Tax_rate
tip=cost*Tip_rate
total=cost+tax+tip
print(tax,tip,total)


# exercise---8

# In[1]:


##The %d formatter is used to input decimal values, or 
##whole numbers. If you provide a float value, it will
##convert it to a whole number, by truncating the values
## after the decimal point.

print("input  your height")
h_ft=int(input("Feet "))
h_inch=int(input("inch "))
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
print("Your height is : %d cm." % h_cm)


# In[ ]:




