import requests
import pandas as pd
import json

def fetch_films(page):
    uri = "https://swapi.dev/api/films/"
    url = f'{uri}{str(page)}/'
    r = requests.get(url)
    data = r.json()
    return data

def transform_films(data, swfilms_df, n_film):
    swfilms_df.loc[n_film,'title'] = data['title']
    swfilms_df.loc[n_film,'episode_numero'] = data['episode_id']
    return swfilms_df

col = ['episode_numero','title']
swfilms_df = pd.DataFrame(columns=col)
n = 6


for i in range(1,n+1):
    data = fetch_films(i)
    swfilms_df = transform_films(data, swfilms_df, i)
swfilms_df