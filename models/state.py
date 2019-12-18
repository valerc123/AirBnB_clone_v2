#!/usr/bin/python3
"""State Class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models.state import State

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            city_all = models.storage.all('City').all()
            n_city = []
            for value in city_all.values():
                if self.id == values.state_id:
                    n_city.append(value)
    else:
        cities = relationship('City', cascade="delete", backref="State")
