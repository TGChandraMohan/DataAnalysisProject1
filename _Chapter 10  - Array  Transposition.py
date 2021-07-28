#!/usr/bin/env python
# coding: utf-8

# In[1]:


# how to transpos Ray on numpy 


# In[2]:


import numpy as np


# In[14]:


# example 1 - How to range  array
arr = np.arange(50).reshape(10,5)
arr


# In[15]:


# Example 2
arr.T # Transpose the  arrangements of row and column


# In[16]:


# Example 3 - dot  function
np.dot(arr.T,arr)


# In[59]:


# Example 4 - 3D matrix
arr_3D = np.arange(50).reshape(5,5,2)
arr_3D


# In[62]:


arr_3D.transpose(1,0,2)


# In[ ]:





# In[ ]:




