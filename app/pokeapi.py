import requests
from random import randint
baseUrl = "https://pokeapi.co/api/v2/"

def getPokemon(pokemon):
    response = requests.get(f"{baseUrl}pokemon-species/{pokemon}")
    if response.status_code == 200:
        pokemonData = response.json()
        return pokemonData
    else:
        return False

def totalPokemon():
    response = requests.get(f"{baseUrl}pokemon-species")
    if response.status_code == 200:
            limite = response.json()
            return limite
    else:
        return False

def getDescription(pokemon):
    for entrada in pokemon["flavor_text_entries"]:
            if(entrada["language"]["name"] == "en"):
                descricao = " ".join(entrada["flavor_text"].split())
                return descricao

def main():
    
    pokemonId = randint(1, 1025)
    pokemon = getPokemon(pokemonId)
    descricao = getDescription(pokemon)
    print("-=-=-=-= Que Pokémon tem esta descrição? -=-=-=-=")
    print(descricao, pokemonId)
    while(True):

        resposta = input(" -> ")
        if(resposta == pokemon["name"]):
            print("Acertou!")
            pokemonId = randint(1, 1025)
            pokemon = getPokemon(pokemonId)
            descricao = getDescription(pokemon)
            print("-=-=-=-= Que Pokémon tem esta descrição? -=-=-=-=")
            print(descricao, pokemonId)
        else:
            print("Errado!")
            

if __name__ == '__main__':
    main()
