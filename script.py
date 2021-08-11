<<<<<<< HEAD
url_planets = 'https://swapi.dev/api/planets/'
def fetch_num_planets ():
    r = requests.get(url_planets)
    if r.status_code == 200:
        data = r.json()
        count = data["count"]
        return count
    else:
        return "NO DATA"
fetch_num_planets()
=======
import pandas as pd
import requests
import json

uri = 'https://swapi.dev/api/planets'
>>>>>>> 533416f1ba1dee0a693a204a1cd3dd7b38f644ff

def fetch_all_planets():
    datalist=[]
    for i in range (1, fetch_num_planets()+2):
        url = f'{url_planets}{str(i)}'
        r_people = requests.get(url)
        if r_people.status_code == 200:
            data_people = r_people.json()
            datalist.append(data_people)
    return datalist
fetch_all_planets()

<<<<<<< HEAD
def planets_dframe():
    columns = ["name","climate","terrain","population","residents","films"]
    planets_df= pd.DataFrame(columns=columns)
    for index, row in enumerate(fetch_all_planets()):
        planets_df.loc[index,'name']=row['name']
        planets_df.loc[index,'climate']=row['climate']
        planets_df.loc[index,'terrain']=row['terrain']
        planets_df.loc[index,'population']=row['population']
        planets_df.loc[index,'residents']=row['residents']
        planets_df.loc[index,'films']=row['films']
    return planets_df
#print(planets_dframe())
=======
data = []
for i in range(1, n_planets):
    response = requests.get(f'{uri}/{str(i)}')
    if response.status_code == 200:
        data.append(response.json())
    else: 
        data = []
        

columns = ['name','rotation_period','orbital_period', "diameter", "climate", "gravity", "terrain", "surface_water", "population", "residents", "films", "created", "edited","url"]
planets_df = pd.DataFrame(columns=columns)
planets_df

data

for index, row in enumerate(data):
    
    planets_df.loc[index,'name'] = row['name']
    planets_df.loc[index,'rotation_period'] = row['rotation_period']
    planets_df.loc[index,'orbital_period'] = row['orbital_period']
    planets_df.loc[index,'diameter'] = row['diameter']
    planets_df.loc[index,'climate'] = row['climate']
    planets_df.loc[index,'gravity'] = row['gravity']
    planets_df.loc[index,'terrain'] = row['terrain']
    planets_df.loc[index,'surface_water'] = row['surface_water']
    planets_df.loc[index,'population'] = row['population']
    planets_df.loc[index,'residents'] = row['residents']
    planets_df.loc[index,'films'] = row['films']
    planets_df.loc[index,'created'] = row['created']
    planets_df.loc[index,'edited'] = row['edited']
    planets_df.loc[index,'url'] = row['url']
    
planets_df



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

>>>>>>> 533416f1ba1dee0a693a204a1cd3dd7b38f644ff
