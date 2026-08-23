import requests

baseUrl = "https://pokeapi.co/api/v2/"

def getPokemon(pokemon):
    response = requests.get(f"{baseUrl}pokemon/{pokemon}")
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

def main():
     limite = totalPokemon()
     print(limite["count"])
    # while(True):
    #     pokemonName = input("Nome ou ID do pokemon: ")
    #     pokemon = getPokemon(pokemonName)
    #     if(pokemon):
    #         print(pokemon["name"])
    #     else:
    #         print("Pokemon nao encontrado")



if __name__ == '__main__':
    main()
