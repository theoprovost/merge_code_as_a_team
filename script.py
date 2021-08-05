import requests
import pandas as pd

def fetch_people(page):
    uri = "https://swapi.dev/api/people/"
    url = f'{uri}{str(page)}/'
    r = requests.get(url)
    data = r.json()
    return data

def transform_people(data, swpeople_df, n_people):
    swpeople_df.loc[n_film,'name'] = data['name']
    swpeople_df.loc[n_film,'height'] = data['height']
    return swpeople_df

col = ['name','height']
swpeople_df = pd.DataFrame(columns=col)
n = 6


for i in range(1,n+1):
    data = fetch_people(i)
    swpeople_df = transform_people(data, swpeople_df, i)
swpeople_df

