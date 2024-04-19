from extraer import extract_ability_data, extract_pokemon_data
from transformar import transform_ability_data
from cargar import cargar_ability, cargar_pokemon

def main():
    # Rango de IDs de Pokémon que deseas extraer, el numero "30" puede ser modificado según la cantidad de pokemones que deseas extraer
    pokemon_ids = range(1, 30)  

    for pokemon_id in pokemon_ids:
        ability_data = extract_ability_data(pokemon_id)
        if ability_data:
            transformed_ability_data = transform_ability_data(ability_data)
            cargar_ability(transformed_ability_data)

        pokemon_data = extract_pokemon_data(pokemon_id)
        if pokemon_data:
            cargar_pokemon(pokemon_data)

if __name__ == "__main__":
    main()

