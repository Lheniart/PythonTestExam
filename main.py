"""
Module principal de l'application FastAPI.

Ce module initialise une instance de FastAPI et
inclut les routeurs définis dans les modules associés.

Modules inclus :
    - trainers : Gère les routes liées aux dresseurs de Pokémon.
    - pokemons : Gère les routes liées aux Pokémon.
    - items : Gère les routes liées aux objets dans l'inventaire des dresseurs.

"""


from fastapi import FastAPI
from app.routers import trainers, pokemons, items


app = FastAPI()


app.include_router(trainers.router,
                   prefix="/trainers")
app.include_router(items.router,
                   prefix="/items")
app.include_router(pokemons.router,
                   prefix="/pokemons")
