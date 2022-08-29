import requests

dados_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/ditto').json()

nome = dados_pokemon['name'].upper()
id = dados_pokemon['id']
sprite = dados_pokemon['sprites']['front_default']
spriteshiny = dados_pokemon['sprites']['front_shiny']
peso = dados_pokemon['weight']
altura = dados_pokemon['height']
print(nome)
print(id)
print(sprite)
