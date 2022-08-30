from django.shortcuts import render
import requests

# Create your views here.



def index(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/snorlax')
    pokemon = response.json()
    nome = pokemon['name'].upper()
    tipo1pokemon = pokemon['types'][0]['type']['name']
    try:
      tipo2pokemon = pokemon['types'][1]['type']['name']
    except:
      tipo2pokemon = 'none'

    peso = pokemon['weight']
    altura = pokemon['height']

    if peso<10:0
    elif peso<100:pesolista=list(str(peso));pesolista.insert(1,'.');peso=''.join(pesolista)
    elif peso<1000:pesolista=list(str(peso));pesolista.insert(2,'.');peso=''.join(pesolista)
    elif peso<10000:pesolista=list(str(peso));pesolista.insert(3,'.');peso=''.join(pesolista)
    else:peso='NaN'

    if altura<10:alturalista=list(str(altura));alturalista.insert(0,'0.');altura=''.join(alturalista)
    elif altura<100:alturalista=list(str(altura));alturalista.insert(1,'.');altura=''.join(alturalista)
    elif altura<1000:alturalista=list(str(altura));alturalista.insert(2,'.');altura=''.join(alturalista)
    elif altura<10000:alturalista=list(str(altura));alturalista.insert(3,'.');altura=''.join(alturalista)
    else:altura='NaN'

    return render(request, 'index.html',{
    'fotopokemon': pokemon['sprites']['other']['official-artwork']['front_default'],
    'nomepokemon': nome,
    'idpokemon': pokemon['id'],
    'tipo1pokemon': tipo1pokemon,
    'tipo2pokemon': tipo2pokemon,
    'peso': peso,
    'altura': altura,
    })