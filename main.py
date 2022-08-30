import requests

dados_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/pidgey').json()

nome = dados_pokemon['name'].upper()
id = dados_pokemon['id']
sprite = dados_pokemon['sprites']['front_default']
spriteshiny = dados_pokemon['sprites']['front_shiny']
peso = dados_pokemon['weight']
altura = dados_pokemon['height']
tipo1pokemon = dados_pokemon['types'][0]['type']['name']
tipo2pokemon = dados_pokemon['types'][0]['type']['name']

print(peso)

if peso < 10:
  pass

elif peso < 100:
    pesolista = list(str(peso))
    pesolista.insert(1, '.')
    peso = ''.join(pesolista)
  
elif peso < 1000:
    pesolista = list(str(peso))
    pesolista.insert(2, '.')
    peso = ''.join(pesolista)
  
elif peso < 10000:
    pesolista = list(str(peso))
    pesolista.insert(3, '.')
    peso = ''.join(pesolista)

print(altura)
altura = int(altura)
if altura < 10:
  alturalista = list(str(altura))
  alturalista.insert(0, '0.')
  altura = ''.join(alturalista)
  
elif altura < 100:
  alturalista = list(str(altura))
  alturalista.insert(1, '.')
  altura = ''.join(alturalista)

elif altura < 1000:
  alturalista = list(str(altura))
  alturalista.insert(2, '.')
  altura = ''.join(alturalista)

elif altura < 10000:
  alturalista = list(str(altura))
  alturalista.insert(3, '.')
  altura = ''.join(alturalista)

print(altura)