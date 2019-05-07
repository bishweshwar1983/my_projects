#!/usr/bin/env python
# coding: utf-8

# In[15]:


my_list=[['']*21for x in range(21)]



for i in range(21):
        my_list[i][20]=1
        my_list[20][i]=1
        
        
for x in range(21):
    print (my_list[x])
    print ('\n')
    
for x in range(19,-1,-1):
    for y in range(19,-1,-1):
        my_list[x][y] = my_list[x+1][y] + my_list[x][y+1]

for x in range(21):
    print (my_list[x])
    print ('\n')


# In[ ]:




