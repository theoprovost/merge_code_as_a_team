import pandas as pd
import requests
import json

'''Planets fetch start'''
uri = 'https://swapi.dev/api/planets'

n_planets = 10

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


'''People fetch start'''
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



'''species'''
uri_species = 'https://swapi.dev/api/species/'
def numspecies():
    r = requests.get(uri_species)
    if r.status_code == 200:
        data = r.json()
        count = data["count"]
        return count
    else:
        return "Failed connection"
    '''allspecies'''
def fetch_all_species():
    datalist=[]
    for i in range (1, numspecies()+1):
        url = f'{uri_species}{str(i)}'
        r_species = requests.get(url)
        if r_species.status_code == 200:
            data_species = r_species.json()
            datalist.append(data_species)
    return datalist

def swapi_df():
    columns = ['name','classification','designation','average_height','skin_colors','hair_colors','eye_colors','average_lifespan','homeworld','language']
    nspecies_df = pd.DataFrame(columns=columns)
    for index, row in enumerate (fetch_all_species()):
        nspecies_df.loc[index,'name'] = row['name']
        nspecies_df.loc[index,'classification'] = row['classification']
        nspecies_df.loc[index,'designation'] = row['designation']
        nspecies_df.loc[index,'average_height'] = row['average_height']
        nspecies_df.loc[index,'skin_colors'] = row['skin_colors']
        nspecies_df.loc[index,'eye_colors'] = row['eye_colors']
        nspecies_df.loc[index,'hair_colors'] = row['hair_colors']
        nspecies_df.loc[index,'average_lifespan'] = row['average_lifespan']
        nspecies_df.loc[index,'homeworld'] = row['homeworld']
        nspecies_df.loc[index,'language'] = row['language']
    return nspecies_df
