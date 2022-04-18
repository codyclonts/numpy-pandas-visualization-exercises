#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np



# In[2]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])



# In[3]:


count = 0

for i in a:
    if i <0:
        count += 1
print(count)


# In[4]:


#1
np.count_nonzero(a<0) 
    


# In[7]:


#2
np.count_nonzero(a>=0)


# In[31]:


#3

x = a % 2
y= x == 0 
evens = a[y]
evens

np.count_nonzero(evens >= 0)



# In[29]:


a[x]


# In[ ]:


#4
add_three = a + 3

np.count_nonzero(add_three >0)


# In[20]:


#5
square = a ** 2
square.mean()


# In[21]:


square.std()


# In[24]:


a.mean()

a - a.mean()


# In[26]:


# 7 
z_score = ((a-a.mean())/(a.std()))
z_score


# In[ ]:
#8 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#exercise 1
sum_of_a = sum(a)
sum_of_a

#exercise 2
min_of_a = min(a)
min_of_a

#exercise 3
max_of_a = max(a)
max_of_a
# exercise 4 
mean_of_a = sum(a) / len(a)
mean_of_a
# exercise 5

product_of_a = 1
for n in a:
    product_of_a *= n
product_of_a

#6
squares_of_a = [number ** 2 for number in a]
squares_of_a

# 7
odds_in_a = [odd for odd in a if odd %2]
odds_in_a

# 8
evens_in_a = [even for even in a if not even % 2]
evens_in_a


## section 2


# %%

# %%

# %%
