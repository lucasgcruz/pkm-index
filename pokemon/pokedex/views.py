from django.shortcuts import render
import requests

# Create your views here.



def index(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/gloom')
    pokemon = response.json()
    nome = pokemon['name'].upper()
    tipo1pokemon = pokemon['types'][0]['type']['name']
    try:
      tipo2pokemon = pokemon['types'][1]['type']['name']
    except:
      tipo2pokemon = 'none'

    return render(request, 'index.html',{
    'fotopokemon': pokemon['sprites']['other']['official-artwork']['front_default'],
    'nomepokemon': nome,
    'idpokemon': pokemon['id'],
    'tipo1pokemon': tipo1pokemon,
    'tipo2pokemon': tipo2pokemon,
    })