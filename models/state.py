#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship



class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state", cascade="all, delete-orphan")
    
@property
def cities(self):
    """Returns a list of all cities in the state"""
    from models import storage
    cities = []
    for city in storage.all(City).values():
        if city.state_id == self.id:
            cities.append(city)
    return cities