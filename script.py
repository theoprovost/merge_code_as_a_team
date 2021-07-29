import pandas as pd
import requests

'''Starships fetch start'''
starship_uri = 'https://swapi.dev/api/starships'


def fetch(starship_uri, n=1):
    response = requests.get(uri + '/?page=' + str(n))
    if response.status_code == 200:
        return response.json()
    else:
        return


first_fetch = fetch(starship_uri)

total_result_c = first_fetch['count']
n_page = len(first_fetch['results'])
total_iter_needed = round(total_result_c / n_page)


fetched_data = []
for i in range(1, total_iter_needed + 1):
    fetched_data += fetch(uri, i)['results']

data = []


def cast_data(d):
    for x in d:
        data.append([x['name'], x['model'], x['manufacturer'], x['films']])


cast_data(fetched_data)
df = pd.DataFrame(
    data, columns=['Name', 'Model', 'Manufacturer', 'Can be seen in'])

print(df)
'''Starships fetch end'''
