"""
Module contenant une API routeur FastAPI pour la
gestion des opérations liées aux dresseurs dans
une application de formation de Pokémon.

Ce routeur expose des endpoints pour créer, récupérer
et effectuer des opérations sur les dresseurs, ainsi
que pour ajouter des objets et des Pokémon à l'inventaire
d'un dresseur. Les opérations utilisent des fonctions
définies dans les modules 'actions', 'schemas', et 'utils',
 ainsi que des dépendances.

Classes et objets :
    - router : Instance de APIRouter pour définir les routes de l'API.

Fonctions :
    - create_trainer(trainer: schemas.TrainerCreate, database: Session = Depends(get_db))
     -> schemas.Trainer:
        Endpoint POST pour créer un dresseur.
        Paramètres :
            - trainer (schemas.TrainerCreate) : Données du nouveau dresseur.
            - database (Session) : Session SQLAlchemy pour l'accès à la base de données.
        Retourne :
            - schemas.Trainer : Dresseur créé.

    - get_trainers(skip: int = 0, limit: int = 100, database: Session = Depends(get_db))
     -> List[schemas.Trainer]:
        Endpoint GET pour récupérer tous les dresseurs.
        Paramètres :
            - skip (int) : Nombre d'éléments à sauter pour la pagination (par défaut : 0).
            - limit (int) : Limite du nombre d'éléments à récupérer (par défaut : 100).
            - database (Session) : Session SQLAlchemy pour l'accès à la base de données.
        Retourne :
            - List[schemas.Trainer] : Liste des dresseurs récupérés depuis la base de données.

    - get_trainer(trainer_id: int, database: Session = Depends(get_db)) -> schemas.Trainer:
        Endpoint GET pour récupérer un dresseur par son ID.
        Paramètres :
            - trainer_id (int) : ID du dresseur à récupérer.
            - database (Session) : Session SQLAlchemy pour l'accès à la base de données.
        Retourne :
            - schemas.Trainer : Dresseur récupéré.

    - create_item_for_trainer(trainer_id: int, item: schemas.ItemCreate,
     database: Session = Depends(get_db)) -> schemas.Item:
        Endpoint POST pour ajouter un objet à l'inventaire d'un dresseur.
        Paramètres :
            - trainer_id (int) : ID du dresseur.
            - item (schemas.ItemCreate) : Données de l'objet à ajouter.
            - database (Session) : Session SQLAlchemy pour l'accès à la base de données.
        Retourne :
            - schemas.Item : Objet ajouté à l'inventaire.

    - create_pokemon_for_trainer(trainer_id: int, pokemon: schemas.PokemonCreate,
    database: Session = Depends(get_db)) -> schemas.Pokemon:
        Endpoint POST pour ajouter un Pokémon à un dresseur.
        Paramètres :
            - trainer_id (int) : ID du dresseur.
            - pokemon (schemas.PokemonCreate) : Données du Pokémon à ajouter.
            - database (Session) : Session SQLAlchemy pour l'accès à la base de données.
        Retourne :
            - schemas.Pokemon : Pokémon ajouté au dresseur.
"""


from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends, HTTPException
from app.utils.utils import get_db
from app import actions, schemas
router = APIRouter()


@router.post("/", response_model=schemas.Trainer)
def create_trainer(trainer: schemas.TrainerCreate, database: Session = Depends(get_db)):
    """
        Create a trainer
    """
    return actions.create_trainer(database=database, trainer=trainer)


@router.get("", response_model=List[schemas.Trainer])
def get_trainers(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all trainers
        Default limit is 100
    """
    trainers = actions.get_trainers(database, skip=skip, limit=limit)
    return trainers


@router.get("/{trainer_id}", response_model=schemas.Trainer)
def get_trainer(trainer_id: int, database: Session = Depends(get_db)):
    """
        Return trainer from his id
    """
    db_trainer = actions.get_trainer(database, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return db_trainer


@router.post("/{trainer_id}/item/", response_model=schemas.Item)
def create_item_for_trainer(
    trainer_id: int, item: schemas.ItemCreate, database: Session = Depends(get_db)
):
    """
        Add an item in trainer inventory
    """
    return actions.add_trainer_item(database=database, item=item, trainer_id=trainer_id)


@router.post("/{trainer_id}/pokemon/", response_model=schemas.Pokemon)
def create_pokemon_for_trainer(
    trainer_id: int, pokemon: schemas.PokemonCreate, database: Session = Depends(get_db)
):
    """
        Add a Pokemon to a trainer
    """
    return actions.add_trainer_pokemon(database=database, pokemon=pokemon, trainer_id=trainer_id)
