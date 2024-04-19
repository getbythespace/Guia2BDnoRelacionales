from conexionBD import get_mongo_client, close_mongo_client

def cargar_ability(data):
    client = get_mongo_client()
    db = client["pokemons"]
    collection = db["abilities"]
   
    collection.insert_one(data)
    print("Se ha insertado un nuevo documento de Ability en la colección 'abilities'.")
    close_mongo_client(client)

def cargar_pokemon(data):
    client = get_mongo_client()
    db = client["pokemons"]
    collection = db["pokemon"]
   
    collection.insert_one(data)
    print("Se ha insertado un nuevo documento de Pokémon en la colección 'pokemon'.")
    close_mongo_client(client)

