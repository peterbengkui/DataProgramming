#!/usr/bin/env python
# coding: utf-8

# In[11]:


def operate(a,b,c):
    if c=='add':
        print (a+b)
    if c=='multiply':
        print (a*b)


# In[12]:


operate(1,6,'add')
operate(1,6, 'multiply')


# In[9]:


def fib (n):
    a=0
    b=1
    if n==1:
        print (a)
    else:
        print (a)
        print (b) 
    
    for i in range (2,n):
        c = a+b
        a = b
        b = c
        print (c)


# In[4]:


fib (6)


# In[5]:


dictionary = {'g':7,'e':5,'.':999}
def encode (name):
    output = ''
    for i in range (0,len(name)):
        output = output+str(dictionary[name[i]])
    return output

encode ('gege')


# In[24]:


def get_n (threshold):
    condition = True
    output_sum = 1
    denominator = 11
    while (condition):
        output_sum = output_sum+(1/denominator)
        if (output_sum>threshold):
            return denominator
            break
            denominator = denominator+1
            
get_n (3)


# In[29]:


def describe(input_list):
    print("number of elements:",len(input_list))
    print("mean : ", sum(input_list)/len(input_list))
    mean = float(sum(input_list)/len(input_list))
    variance = sum ([((x - mean )**2)for x in input_list])/len(input_list)
    stddev = variance **0.5
    print ('variance:',variance)
    print ('standard deviation',stddev)
    

describe([2,4,6,8,10,12,14,16,18,20,22,24])


# In[ ]:




