"""
Module contenant des fonctions utilitaires liées à
la gestion de la base de données et au calcul de l'âge à partir
de la date de naissance.

Fonctions :
    - get_db() -> SessionLocal:
        Récupère une session de base de données.
        Retourne :
            - SessionLocal : Session SQLAlchemy pour l'accès à la base de données.

    - age_from_birthdate(birthdate: date) -> int:
        Calcule l'âge à partir de la date de naissance.
        Paramètres :
            - birthdate (date) : Date de naissance.
        Retourne :
            - int : Âge calculé.
"""

from datetime import date
from app import models
from app.sqlite import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    """
        Get the DB
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


def age_from_birthdate(birthdate):
    """
        Return an age from a birthday
    """
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day)
                                          < (birthdate.month, birthdate.day))
