import requests
import os

# Make a GET request to the Pokemon API to get the list of Pokemon
def get_pokemon_list(num):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={num}')

    # Get the list of Pokemon from the response JSON
    pokemon_list = response.json()['results']

    dict = []
    # Loop through each Pokemon and save its image
    for pokemon in pokemon_list:
        name = pokemon['name']
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        image_url = response.json()['sprites']['other']['official-artwork']['front_default']
        image_data = requests.get(image_url).content
        with open(f'images/{name}.png', 'wb') as f:
            f.write(image_data)
        dict.append(name)

    return dict