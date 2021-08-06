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