def transform_ability_data(data):
    transformed_data = {
        "AbilityID": data.get("id"),
        "AbilityName": data.get("ability_name"),
        "IsMainSeries": data.get("is_main_series"),
        "Generation": data.get("generation"),
        "Effect": data.get("effect"),
        "ShortEffect": data.get("short_effect"),
        "Hidden": data.get("hidden"),
        "Slot": data.get("slot"),
        "PokemonName": data.get("pokemon_name"),
        "PokemonURL": data.get("pokemon_url")
    }
    return transformed_data


def transform_pokemon_data(data):
    transformed_data = {
        "PokemonID": data.get("id"),
        "Name": data.get("name"),
        "BaseExperience": data.get("base_experience"),
        "Height": data.get("height"),
        "IsDefault": data.get("is_default"),
        "Order": data.get("order"),
        "Weight": data.get("weight"),
        "Abilities": data.get("abilities"),
        "Forms": data.get("forms"),
        "GameIndices": data.get("game_indices"),
        "HeldItems": data.get("held_items"),
        "LocationAreaEncounters": data.get("location_area_encounters"),
        "Moves": data.get("moves")
    }
    return transformed_data
