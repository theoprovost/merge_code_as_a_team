#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd


# # Fetching API

# In[26]:


uri = 'https://swapi.dev/api/people/'


# In[27]:


n_people = 84


# In[29]:


data = [ ]
for i in range(1,84):
    res = requests.get(f"{uri}/{str(i)}")
    if res.status_code == 200:
        data.append(res.json())
    else : data = [] 
print(data)


# In[43]:


columns = ['name','height', "mass", "hair_color", "skin_color", 'eye_color', 'birth_year', 'gender', 'films', 'species', 'starships', 'edited', 'url']
SWpeople_df = pd.DataFrame(columns=columns)
SWpeople_df


# In[45]:


SWpeople_df.append(data[], ignore_index=True)


# In[35]:


SWpeople_df


# In[5]:


data = [] r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    print(data)
else:
    print("NO DATA")


# In[6]:


def fetch_SW(n_people):
    if n_people > 0:
        url = f'{uri}people/{str(n_people)}/'
        r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        return None


# In[7]:


fetch_SW(5)


# In[8]:


columns = ['name','height', "mass", "hair_color", "skin_color", 'eye_color', 'birth_year', 'gender', 'films', 'species', 'starships', 'edited', 'url']
SWpeople_df = pd.DataFrame(columns=columns)
SWpeople_df


# In[11]:


for i in range(1, 83):
    SWpeople_df.append(fetch_SW(i), ignore_index=True)


# In[12]:


SWpeople_df


# In[123]:


len(results)


# In[ ]:


bbquote_df


# In[ ]:


def transform_bbquote_data(json_response):
    columns = ['author','quote']
    bbquote_df = pd.DataFrame(columns=columns)
    
    for index, row in enumerate(json_response):
        bbquote_df.loc[index,'author'] = row['author']
        bbquote_df.loc[index,'quote'] = row['quote']
    return bbquote_df


# In[ ]:


transform_bbquote_data(quotes_list)

