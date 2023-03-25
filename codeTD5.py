import requests
import pandas as pd

#Get the IDs of all places in a given county
def get_place_ids(county):
    url=f'http://opendomesday.org/api/1.0/county/{county}'
    response = requests.get(url)
    data = response.json()
    place_ids=[place['id'] for place in data['places_in_county']]
    return place_ids

#Get the IDs,geld,ploughs of a manor in a given place
def get_manor_info(place_id):
    url=f"http://opendomesday.org/api/1.0/manor/{place_id}/"
    response = requests.get(url)
    data = response.json()
    geld = data['geld']
    total_ploughs = data['totalploughs']
    manor_id=data['place'][0]['id']
    return (manor_id,geld, total_ploughs)

#Main function
if __name__ == '__main__':
    county = 'dby'
    #place_ids = get_place_ids(county)
    place_ids=[1036,2558,3016,4791,6093,8701,8951,9101]

    #Import manor_id, geld & total ploughs
    manor_info=[]
    for id in place_ids:
        manor_info.append(get_manor_info(id))

    #Create a Pandas DataFrame with same information
    df = pd.DataFrame(manor_info, columns=['manor_id','geld', 'total_ploughs'])
    print(df)

    #Compute the sum of geld paid and total ploughs owned in Derbyshire
    total_geld = df['geld'].sum()
    total_ploughs = df['total_ploughs'].sum()

    print('Total geld paid in Derbyshire:', total_geld)
    print('Total ploughs owned in Derbyshire:', total_ploughs)
