"""
Module contenant des fonctions utilitaires pour
interagir avec l'API PokeAPI et effectuer des opérations
de bataille entre Pokémon.

Fonctions :
    - get_pokemon_name(api_id: int) -> str:
        Récupère le nom d'un Pokémon à partir de l'API PokeAPI.
        Paramètres :
            - api_id (int) : ID du Pokémon.
        Retourne :
            - str : Nom du Pokémon.

    - get_pokemon_stats(api_id: int) -> list:
        Récupère les statistiques d'un Pokémon à partir de l'API PokeAPI.
        Paramètres :
            - api_id (int) : ID du Pokémon.
        Retourne :
            - list : Liste des statistiques du Pokémon.

    - get_pokemon_data(api_id: int) -> dict:
        Récupère les données d'un Pokémon à partir de l'API PokeAPI.
        Paramètres :
            - api_id (int) : ID du Pokémon.
        Retourne :
            - dict : Données du Pokémon.

    - battle_pokemon(first_api_id: int, second_api_id: int) -> dict:
        Effectue une bataille entre deux Pokémon.
        Paramètres :
            - first_api_id (int) : ID du premier Pokémon.
            - second_api_id (int) : ID du deuxième Pokémon.
        Retourne :
            - dict : Résultat de la bataille. {"Result": winner_api_id}
            ({"Result": "Draw"} en cas d'égalité).

    - battle_compare_stats(first_pokemon_stats: list, second_pokemon_stats: list) -> int:
        Compare les statistiques entre deux Pokémon.
        Paramètres :
            - first_pokemon_stats (list) : Statistiques du premier Pokémon.
            - second_pokemon_stats (list) : Statistiques du deuxième Pokémon.
        Retourne :
            - int : Résultat de la comparaison des statistiques.
"""

import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']


def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    return get_pokemon_data(api_id)['stats']


def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
        Return result of battle
        if there is a winner it return winner id else it return draw
    """
    premier_pokemon = get_pokemon_data(first_api_id)
    second_pokemon = get_pokemon_data(second_api_id)
    if premier_pokemon and second_pokemon:
        battle_result = battle_compare_stats(premier_pokemon["stats"], second_pokemon["stats"])
        if battle_result > 0:
            return {"Result": first_api_id}
        if battle_result < 0:
            return {"Result": second_api_id}
        return {"Result": "Draw"}
    return None


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    result = 0
    for index, stats in enumerate(first_pokemon_stats):
        result += stats["base_stat"] - second_pokemon_stats[index]["base_stat"]
    return result
