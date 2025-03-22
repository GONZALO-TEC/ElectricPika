import requests
import json
import os

def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        pokemon = {
            "nombre": datos["name"],
            "peso": datos["weight"],
            "altura": datos["height"],
            "tipos": [tipo["type"]["name"] for tipo in datos["types"]],
            "habilidades": [habilidad["ability"]["name"] for habilidad in datos["abilities"]],
            "imagen": datos["sprites"]["front_default"]
        }
        guardar_en_json(nombre, pokemon)
        return pokemon
    else:
        return None

def guardar_en_json(nombre, datos):
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")
    
    with open(f"pokedex/{nombre.lower()}.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def main():
    nombre = input("Introduce el nombre de un Pokémon: ")
    pokemon = obtener_pokemon(nombre)
    
    if pokemon:
        print(f"\nNombre: {pokemon['nombre'].capitalize()}")
        print(f"Peso: {pokemon['peso']}")
        print(f"Altura: {pokemon['altura']}")
        print(f"Tipos: {', '.join(pokemon['tipos'])}")
        print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
        print(f"Imagen: {pokemon['imagen']}")
    else:
        print("Pokémon no encontrado. Verifica el nombre e intenta de nuevo.")

if __name__ == "__main__":
    main()