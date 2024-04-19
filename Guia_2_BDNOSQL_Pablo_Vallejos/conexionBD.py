import pymongo

def get_mongo_client():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print("Conexión exitosa con MongoDB")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print("Error al conectarse a MongoDB:", e)

def close_mongo_client(client):
    try:
        client.close()
        print("Conexión cerrada con MongoDB")
    except pymongo.errors.ConnectionFailure as e:
        print("Error al cerrar la conexión con MongoDB:", e)
