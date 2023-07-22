#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd

data = pd.read_csv("C:/Users/f1shs/Downloads/wos_stop_2.csv") 
data = list(data['mystops'])


# In[64]:


for i in range(len(data)):
    data[i] = str(data[i])


# In[70]:


def count_xletter_words(list, x): #подсчитываем количество слов длины x в файле list
    count = 0
    for i in list: 
        if len(i) == x:
            count += 1
    return count


# In[71]:


count_xletter_words(data, 1)


# In[72]:


count_xletter_words(data, 2)


# In[73]:


count_xletter_words(data, 3)


# In[80]:


with open("C:/Users/f1shs/Downloads/result.txt", 'w') as file: 
    for i in range(1,4):
        file.write(str(count_xletter_words(data, i))) 
        file.write('\n')

