#!/usr/bin/env python
# coding: utf-8

# In[35]:


import requests
import pandas as pd


# In[44]:


uri = 'https://swapi.dev/api/species/'


# In[158]:


nspecies = 37


# In[162]:


data = []
for i in range(1,nspecies):
    res =  requests.get(f"{uri}/{str(i)}") 
    if res.status_code == 200:
        data.append(res.json())
    else : data = []
print(data)


# In[160]:


columns = ['name','classification','designation','average_height','skin_colors','hair_colors','eye_colors','average_lifespan','homeworld','language']
nspecies_df = pd.DataFrame(columns=columns)
nspecies_df


# In[163]:


for index, row in enumerate (data):
    
    nspecies_df.loc[index,'name'] = row['name']
    nspecies_df.loc[index,'classification'] = row['classification']
    nspecies_df.loc[index,'designation'] = row['designation']
    nspecies_df.loc[index,'average_height'] = row['average_height']
    nspecies_df.loc[index,'skin_colors'] = row['skin_colors']
    nspecies_df.loc[index,'hair_colors'] = row['hair_colors']
    nspecies_df.loc[index,'average_lifespan'] = row['average_lifespan']
    nspecies_df.loc[index,'homeworld'] = row['homeworld']
    nspecies_df.loc[index,'language'] = row['language']
nspecies_df

    


# In[140]:





# In[ ]:




