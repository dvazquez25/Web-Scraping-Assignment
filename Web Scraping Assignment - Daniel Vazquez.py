#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[7]:


url = "https://webpages.charlotte.edu/mscipion/"
r = requests.get(url)


soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
print(table)


# In[8]:


headers = table.find_all("th")
print(headers)


# In[9]:


titles = []
for i in headers:
    title = i.text
    titles.append(title)
    
print(titles)


# In[11]:


table1_df = pd.DataFrame(columns = titles)
table1_df.describe()
print (table1_df)


# In[12]:


rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(table1_df)
    table1_df.loc[i] = row
print(table1_df)


# In[13]:


for i in rows[1:]:
    data = table.find_all("td")
    print(data)


# In[15]:


for i in rows [1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(table1_df)
    table1_df.loc[l]= row
    table1_df.head(6)
print(table1_df)

