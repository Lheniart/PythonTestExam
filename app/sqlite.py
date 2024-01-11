"""
Module gérant la configuration de la base de données
 SQLAlchemy pour une application de formation de Pokémon.

Ce module utilise SQLAlchemy pour créer un moteur de base de données,
 déclarer une base, et configurer une usine de session.

Classes et objets :
    - engine : Moteur SQLAlchemy pour la base de données.
    - SessionLocal : Usine de session pour créer des sessions de base de données.

Notes :
    - La base de données utilisée est SQLite, et le fichier de base de données
    est situé à "./sqlite.db".
    - L'option "check_same_thread" est définie à False pour permettre l'utilisation
    de sessions SQLAlchemy dans des threads différents.
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_LITE = "sqlite:///./sqlite.db"
engine = create_engine(SQL_LITE, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
