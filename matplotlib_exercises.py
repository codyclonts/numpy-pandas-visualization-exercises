#!/usr/bin/env python
# coding: utf-8

# In[29]:


import matplotlib.pyplot as plt  

#import other libraries 
import numpy as np
import math
from random import randint
import random
import pandas as pd


# In[56]:



#x = np.linspace(-10,10)
x = list(range(-10,10))
y = [(i**2 - i + 2) for i in x]
plt.figure(figsize = (10,8))
plt.plot(x,y, marker = 'o')
plt.grid(True, ls = '--')
plt.annotate("origin",xy=(0,0), xytext= (-3,5) , arrowprops={'facecolor': 'blue'})
plt.title('parabola chart')
plt.xlabel('x')
plt.ylabel('y')


# In[95]:


#3 and #4

x = list(range(0,50))

x1= range(0,10)
y = [x** .5 for x in x]
y2 = [x**3 for x in x]
y3 = [2**x1 for x1 in x1]
y4= [(1/(x+1)) for x in x]


plt.figure(figsize = (10,8))



plt.suptitle('subplots')

plt.subplot(2,2,1)
plt.plot(x,y, color = 'r')
plt.title('y=√x')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True, ls = '--')



plt.subplot(2,2,2)
plt.plot(x,y2, color = 'k')
plt.title('y=x^3')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True, ls = '--')

plt.subplot(2,2,3)
plt.plot(x1,y3, color = 'b')
plt.title('y=2^x')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True, ls = '--')

plt.subplot(2,2,4)
plt.plot(x,y4, color='green')
plt.title('y=1/(x+1)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True, ls = '--')


plt.tight_layout()


# In[ ]:




