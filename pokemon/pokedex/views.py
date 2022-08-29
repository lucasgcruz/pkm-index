from django.shortcuts import render
import requests

# Create your views here.



def index(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/hitmonchan')
    pokemon = response.json()
    nome = pokemon['name'].upper()

    return render(request, 'index.html',{
    'fotopokemon': pokemon['sprites']['other']['official-artwork']['front_default'],
    'nomepokemon': nome,
    'idpokemon': pokemon['id'],
    'tipo1pokemon': pokemon['types'][0]['type']['name'],
    'tipo2pokemon': pokemon['types'][0]['type']['name'],
    })