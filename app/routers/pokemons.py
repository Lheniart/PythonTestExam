from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.pokeapi import battle_pokemon
from app.utils.utils import get_db

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
            {"pokemonApiID":pokemonApiID, "result": resultValue:int} (None if draw)
    """
    return battle_pokemon(pokemon_api_id_1, pokemon_api_id_2)
