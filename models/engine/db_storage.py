#!/usr/bin/python3
"""This module contains the codebase for the mysql db"""
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os

user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')

class DBStorage:
    """This class manages storage of hbnb models in a mysql database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        if cls is None, returns all objects
        """
        new_dict = {}
        if cls is None:
            for cls in self.__classes:
                output = DBStorage.__session.query(cls).all()
                for obj in output:
                    key ="{}.{}".format(obj__class__.__name__, obj.id)
                    