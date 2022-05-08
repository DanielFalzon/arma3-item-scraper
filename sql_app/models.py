#Defining the DB models from which the database tables will be created. 

from sqlalchemy import String, Column, ForeignKey, Integer, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

from .database import Base

#https://docs.sqlalchemy.org/en/14/orm/self_referential.html
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('categories.id'))
    last_update = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    created = Column(TIMESTAMP, server_default=func.now())

    children = relationship("Node", 
        backref=backref('parent', remote_side=[id])
    )
    parent = relationship('Category', remote_side=[id], backref='children')
