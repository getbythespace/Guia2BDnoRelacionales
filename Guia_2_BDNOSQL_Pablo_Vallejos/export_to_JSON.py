import json
from bson import ObjectId
from bson import json_util
from conexionBD import get_mongo_client, close_mongo_client

def custom_json_serializer(obj):
    """Función de serialización personalizada para manejar los ObjectId."""
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def export_to_json():
    client = get_mongo_client()
    db = client["pokemons"]

    collections = ["abilities", "pokemon"]
    for collection_name in collections:
        collection = db[collection_name]
        cursor = collection.find({})
        data = list(cursor)
        with open(f"{collection_name}.json", "w") as outfile:
            json.dump(data, outfile, default=custom_json_serializer, indent=2)
        print(f"Se ha exportado la colección '{collection_name}' a '{collection_name}.json'.")

    close_mongo_client(client)

if __name__ == "__main__":
    export_to_json()


