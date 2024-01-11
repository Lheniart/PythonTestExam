"""
Module contenant les fonctions d'action de l'application.

Ce module expose des fonctions qui effectuent diverses opérations liées aux dresseurs, aux pokémons
et aux objets dans le système. Ces fonctions utilisent la couche d'accès aux données définie
dans les modules 'models', 'schemas', et 'utils.pokeapi'.

Fonctions :
    - get_trainer(database: Session, trainer_id: int) -> models.Trainer:
        Trouve un dresseur par son identifiant.

    - get_trainer_by_name(database: Session, name: str) -> List[models.Trainer]:
        Trouve des dresseurs par leur nom.

    - get_trainers(database: Session, skip: int = 0, limit: int = 100) -> List[models.Trainer]:
        Récupère tous les dresseurs, avec une option pour paginer les résultats.

    - create_trainer(database: Session, trainer: schemas.TrainerCreate) -> models.Trainer:
        Crée un nouveau dresseur.

    - add_trainer_pokemon(database: Session,
    pokemon: schemas.PokemonCreate, trainer_id: int) -> models.Pokemon:
        Crée un nouveau pokémon et le lie à un dresseur.

    - add_trainer_item(database: Session, item: schemas.ItemCreate, trainer_id: int) -> models.Item:
        Crée un nouvel objet et le lie à un dresseur.

    - get_items(database: Session, skip: int = 0, limit: int = 100) -> List[models.Item]:
        Récupère tous les objets, avec une option pour paginer les résultats.

    - get_pokemon(database: Session, pokemon_id: int) -> models.Pokemon:
        Trouve un pokémon par son identifiant.

    - get_pokemons(database: Session, skip: int = 0, limit: int = 100) -> List[models.Pokemon]:
        Récupère tous les pokémons, avec une option pour paginer les résultats.
"""

from sqlalchemy.orm import Session
from . import models, schemas
from .utils.pokeapi import get_pokemon_name


def get_trainer(database: Session, trainer_id: int):
    """
        Find a user by his id
    """
    return database.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()


def get_trainer_by_name(database: Session, name: str):
    """
        Find a user by his name
    """
    return database.query(models.Trainer).filter(models.Trainer.name == name).all()


def get_trainers(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all users
        Default limit is 100
    """
    return database.query(models.Trainer).offset(skip).limit(limit).all()


def create_trainer(database: Session, trainer: schemas.TrainerCreate):
    """
        Create a new trainer
    """
    db_trainer = models.Trainer(name=trainer.name, birthdate=trainer.birthdate)
    database.add(db_trainer)
    database.commit()
    database.refresh(db_trainer)
    return db_trainer


def add_trainer_pokemon(database: Session, pokemon: schemas.PokemonCreate, trainer_id: int):
    """
        Create a pokemon and link it to a trainer
    """
    db_item = models.Pokemon(
        **pokemon.dict(), name=get_pokemon_name(pokemon.api_id), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def add_trainer_item(database: Session, item: schemas.ItemCreate, trainer_id: int):
    """
        Create an item and link it to a trainer
    """
    db_item = models.Item(**item.dict(), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def get_items(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all items
        Default limit is 100
    """
    return database.query(models.Item).offset(skip).limit(limit).all()


def get_pokemon(database: Session, pokemon_id: int):
    """
        Find a pokemon by his id
    """
    return database.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()


def get_pokemons(database: Session, skip: int = 0, limit: int = 100):
    """
        Find all pokemons
        Default limit is 100
    """
    return database.query(models.Pokemon).offset(skip).limit(limit).all()
