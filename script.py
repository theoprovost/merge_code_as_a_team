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