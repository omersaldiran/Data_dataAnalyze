#!/usr/bin/env python
# coding: utf-8
# 
#

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
get_ipython().run_line_magic('matplotlib', 'inline')


# The first ten line of dataset. 

# In[4]:


student = pd.read_csv("student-mat.csv",sep=';')
student.head(10)


# We can see here mean, standart deviation, min and max values of the numeraical values. 

# In[6]:


student.describe()


# Checking the and missing data on the dataset. According to checking there is no missing value.

# In[10]:


student.isnull().sum()


# Some of the grafical visualisations

# In[13]:


plt.figure(figsize=(12,10));
sns.heatmap(student.corr());


# In[14]:


plt.hist(student.age, 20);


# In[15]:


f, axarr = plt.subplots(1,2)
f.set_size_inches(12,5)
axarr[0].boxplot(student.G3, vert=False)
axarr[1].hist(student.G3);


# In[ ]:




