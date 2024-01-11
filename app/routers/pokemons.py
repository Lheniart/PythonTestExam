"""
Module contenant une API routeur FastAPI pour la gestion des
opérations liées aux pokémons dans une application de formation
de Pokémon.

Ce routeur expose des endpoints pour récupérer des informations sur les pokémons,
ainsi qu'une fonction de bataille entre deux pokémons. Les opérations utilisent
des fonctions définies dans les modules 'actions', 'schemas', et 'utils',
ainsi que des dépendances.

Classes et objets :
    - router : Instance de APIRouter pour définir les routes de l'API.

Fonctions :
    - get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db))
    -> List[schemas.Pokemon]:
        Endpoint GET pour récupérer tous les pokémons.
        Paramètres :
            - skip (int) : Nombre d'éléments à sauter pour la pagination (par défaut : 0).
            - limit (int) : Limite du nombre d'éléments à récupérer (par défaut : 100).
            - database (Session) : Session SQLAlchemy pour l'accès à la base de données.
        Retourne :
            - List[schemas.Pokemon] : Liste des pokémons récupérés depuis la base de données.

    - pokemons_battle(pokemon_api_id_1: int, pokemon_api_id_2: int) -> dict:
        Endpoint GET pour une bataille entre deux pokémons.
        Paramètres :
            - pokemon_api_id_1 (int) : ID du premier pokémon.
            - pokemon_api_id_2 (int) : ID du deuxième pokémon.
        Retourne :
            - dict : Résultat de la bataille sous forme de dictionnaire.
            {"pokemonApiID": pokemonApiID, "result": resultValue:int}
            (None en cas d'égalité).

    - pokemons_random() -> List[dict]:
        Endpoint GET pour obtenir 3 pokémons choisis aléatoirement.
        Retourne :
            - List[dict] : Liste de 3 pokémons avec leurs données.
"""
from random import randint
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.utils import get_db
from app import actions, schemas
from app.utils.pokeapi import battle_pokemon, get_pokemon_data

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons


@router.get("/battle/{pokemon_api_id_1}/{pokemon_api_id_2}")
def pokemons_battle(pokemon_api_id_1: int, pokemon_api_id_2: int):
    """
        Battle between two pokemons
        Params:
            pokemonID (int): id of the first pokemon
            pokemonID2 (int): id of the second pokemon
        Return result
            {"pokemonApiID": pokemonApiID, "result": resultValue:int} (None if draw)
    """
    return battle_pokemon(pokemon_api_id_1, pokemon_api_id_2)


@router.get("/random/")
def pokemons_random():
    """
        Get 3 random pokemons
        Return:
            List of 3 pokemons
    """
    pokemons: list[dict, dict, dict] = []
    while len(pokemons) != 3:
        pokemon = get_pokemon_data(randint(1, 898))
        if pokemon not in pokemons and pokemon is not None:
            pokemons.append(pokemon)
    return pokemons
