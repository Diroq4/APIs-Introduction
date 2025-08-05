#How to connect to an API
import json
import requests

base_url = "https://pokeapi.co/api/v2/" #This is the URL we will search in

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}" #This is because on the url this is how we search for the information
    response = requests.get(url)

    if response.status_code == 200: #This IF statment will give us the 200 that means that evertyhing is correct if not we are not connected to the page
        pokemon_data = response.json() #Here we are calling the information of the page as a Json dictionary
        return pokemon_data
    else:
        print(f"Faile to retrieve data {response.status_code}")

pokemon_name = "metapod" #This is the name we will find or want to find
pokemon_info = get_pokemon_info(pokemon_name) #We are asigning the fucntion to a value so we can printed

if pokemon_info: #Here we type the information we would like to have if the pokemon was found
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}cm")
    print(f"Weight: {pokemon_info["weight"]}kg")
else:
    print(f"Pokemon not found")