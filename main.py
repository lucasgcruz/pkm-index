import requests
import translators as ts



dados_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/machamp').json()



nome = dados_pokemon['name'].upper()
id = dados_pokemon['id']
sprite = dados_pokemon['sprites']['front_default']
spriteshiny = dados_pokemon['sprites']['front_shiny']
peso = dados_pokemon['weight']
altura = dados_pokemon['height']
tipo1pokemon = dados_pokemon['types'][0]['type']['name']
tipo2pokemon = dados_pokemon['types'][0]['type']['name']
urlespecie = dados_pokemon['species']['url']
dados_especie = requests.get(urlespecie).json()
categoria_ingles = dados_especie['genera'][7]['genus']
print(categoria_ingles)
categoria_ingles = ts.lingvanex(categoria_ingles, from_language='en_EN', to_language='pt_BR')
print(categoria_ingles)

descricao = dados_especie['flavor_text_entries'][9]['flavor_text']
descricao = descricao.replace('',' ')
print(descricao)

descricao = ts.lingvanex(descricao, from_language='en_EN', to_language='pt_BR')
print(descricao)



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
