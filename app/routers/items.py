"""
Module contenant une API routeur FastAPI pour la gestion des opérations
liées aux objets dans une application de formation de Pokémon.

Ce routeur expose des endpoints pour récupérer des informations
sur les objets, utilisant des opérations définies dans les modules
 'actions' et 'schemas', ainsi que des dépendances.

Classes et objets :
    - router : Instance de APIRouter pour définir les routes de l'API.

Fonctions :
    - get_items(skip: int = 0, limit: int = 100, database: Session =
    Depends(get_db)) -> List[schemas.Item]:
        Endpoint GET pour récupérer tous les objets.
        Paramètres :
            - skip (int) : Nombre d'éléments à sauter pour la pagination (par défaut : 0).
            - limit (int) : Limite du nombre d'éléments à récupérer (par défaut : 100).
            - database (Session) : Session SQLAlchemy pour l'accès à la base de données.

Notes :
    - L'utilisation de dépendances comme 'Depends(get_db)' permet d'obtenir
    une session de base de données pour chaque requête.
    - La réponse du endpoint est une liste d'objets de type 'schemas.Item'.
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.utils.utils import get_db
from app import actions, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all items
        Default limit is 100
    """
    items = actions.get_items(database, skip=skip, limit=limit)
    return items
