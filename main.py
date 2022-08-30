import requests

dados_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/zapdos').json()

nome = dados_pokemon['name'].upper()
id = dados_pokemon['id']
sprite = dados_pokemon['sprites']['front_default']
spriteshiny = dados_pokemon['sprites']['front_shiny']
peso = dados_pokemon['weight']
altura = dados_pokemon['height']
tipo1pokemon = dados_pokemon['types'][0]['type']['name']
tipo2pokemon = dados_pokemon['types'][1]['type']['name']
print(tipo1pokemon)
