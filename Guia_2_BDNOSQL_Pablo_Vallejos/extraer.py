import requests

def extract_ability_data(ability_id):
    url = f"https://pokeapi.co/api/v2/ability/{ability_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            extracted_data = {
                "id": data.get("id"),
                "name": data.get("name"),
                "is_main_series": data.get("is_main_series"),
                "generation": data.get("generation", {}).get("name"),
                "generation_url": data.get("generation", {}).get("url"),
                "ability_name": data.get("names", [{}])[0].get("name"),
                "ability_language": data.get("names", [{}])[0].get("language", {}).get("name"),
                "ability_language_url": data.get("names", [{}])[0].get("language", {}).get("url"),
                "effect": data.get("effect_entries", [{}])[0].get("effect"),
                "short_effect": data.get("effect_entries", [{}])[0].get("short_effect"),
                "hidden": data.get("pokemon", [{}])[0].get("is_hidden"),
                "slot": data.get("pokemon", [{}])[0].get("slot"),
                "pokemon_name": data.get("pokemon", [{}])[0].get("pokemon", {}).get("name"),
                "pokemon_url": data.get("pokemon", [{}])[0].get("pokemon", {}).get("url")
            }
            return extracted_data
        except Exception as e:
            print(f"Error al extraer datos de la habilidad {ability_id}: {e}")
            return None
    else:
        print(f"Error al solicitar datos de la habilidad {ability_id}: Código de estado {response.status_code}")
        return None

def extract_pokemon_data(pokemon_id_or_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            extracted_data = {
                "id": data.get("id"),
                "name": data.get("name"),
                "base_experience": data.get("base_experience"),
                "height": data.get("height"),
                "is_default": data.get("is_default"),
                "order": data.get("order"),
                "weight": data.get("weight"),
                "abilities": [ability.get("ability", {}).get("name") for ability in data.get("abilities", [])],
                "forms": [form.get("name") for form in data.get("forms", [])],
                "game_indices": [game_index.get("version", {}).get("name") for game_index in data.get("game_indices", [])],
                "held_items": [held_item.get("item", {}).get("name") for held_item in data.get("held_items", [])],
                "location_area_encounters": data.get("location_area_encounters"),
                "moves": [move.get("move", {}).get("name") for move in data.get("moves", [])]
            }
            return extracted_data
        except Exception as e:
            print(f"Error al extraer datos del Pokémon {pokemon_id_or_name}: {e}")
            return None
    else:
        print(f"Error al solicitar datos del Pokémon {pokemon_id_or_name}: Código de estado {response.status_code}")
        return None