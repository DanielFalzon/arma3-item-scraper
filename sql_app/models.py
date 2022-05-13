#Defining the DB models from which the database tables will be created. 

from sqlalchemy import String, Column, ForeignKey, Integer, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from sqlalchemy.orm.collections import attribute_mapped_collection

from database import Base, session_maker

#https://docs.sqlalchemy.org/en/14/orm/self_referential.html
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey(id))
    last_update = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    created = Column(TIMESTAMP, server_default=func.now())


    children = relationship("Category", backref=backref('parent', remote_side=[id]))

    def dump(self):
        children = ""
        parent = ""

        if len(self.children) > 0:
            children = "\nChildren:"
            for child in self.children:
                children += child.name

        if (not self.parent is None):
            parent = f"\nParent:{self.parent.name}"

        return( 
            f"Name:{self.name}{children}{parent}"
        )

with session_maker() as session:
    category_records = session.query(Category).all()
    for category in category_records:
        print(category.dump())
        print("--------")

# def create_categories():
#     with session_maker() as session:
#             for category in categories:
#                 print(category)
#                 session.add(category)
#             session.commit()
# create_categories()