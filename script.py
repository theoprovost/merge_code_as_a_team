import pandas as pd
import requests
import json

'''Films fetch start'''
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
'''Films fetch end'''


'''Starships fetch start'''
starship_uri = 'https://swapi.dev/api/starships'


def starships_fetch(uri, n=1):
    response = requests.get(uri + '/?page=' + str(n))
    if response.status_code == 200:
        return response.json()
    else:
        return


first_fetch = starships_fetch(starship_uri)

total_result_c = first_fetch['count']
n_page = len(first_fetch['results'])
total_iter_needed = round(total_result_c / n_page)


fetched_data = []
for i in range(1, total_iter_needed + 1):
    fetched_data += starships_fetch(starship_uri, i)['results']

data = []


def cast_data(d):
    for x in d:
        data.append([x['name'], x['model'], x['manufacturer'], x['films']])


cast_data(fetched_data)
df = pd.DataFrame(
    data, columns=['Name', 'Model', 'Manufacturer', 'Can be seen in'])

print(df)
'''Starships fetch end'''
