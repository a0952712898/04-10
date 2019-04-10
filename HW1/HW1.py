
# coding: utf-8

# In[7]:


import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding = "big5"
book1 = response.text
book1[:3]


# In[8]:


book1[3:5]


# In[10]:


book1[10:20:2]

