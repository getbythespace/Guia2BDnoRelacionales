from conexionBD import get_mongo_client, close_mongo_client

def verificar_pokemones():
    client = get_mongo_client()
    db = client["pokemons"]
    collection = db["pokemon"]

    pokemones = list(collection.find())
    for pokemon in pokemones:
        print(pokemon)
        print()  

    print("\n" + "*" * 20)  
    print(f"Total de Pokémon en la colección 'pokemon': {len(pokemones)}")
    print("*" * 20)  
    close_mongo_client(client)

if __name__ == "__main__":
    verificar_pokemones()

