#!/usr/bin/python3
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, scopedsession
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None
    cities = relationship("City")

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(environ['HBNB_MYSQL_USER'],
                                              environ['HBNB_MYSQL_PWD'],
                                              environ['HBNB_MYSQL_HOST']
                                              environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)
        if environ['HBNB_ENV'] =='test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Select all objects of a cls
        """
        session = self.__session()
        if cls is None:
            session.query(User, State, City, Amenity, Place, Review).all()
        else:
            session.query(cls)
        return session.__dict

    def new(self, obj):
        """Add obj to the database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj if not none
        """
        if obj not None:
            del obj

    def reload(self):
        """
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)




