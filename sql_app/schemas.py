#Schemas utilised for response validation when querying the API.
from __future__ import annotations
from pydantic import BaseModel

#For now we just need to get the category. Look into getting a list of categories
#or items matching a text search later.
class Category(BaseModel):
    id: int
    name: str
    parent: Category = None
    children: list[Category] = []

    #This will allow us to query the returned data as an ORM model rather than
    #an item in a dict
    class Config:
        orm_mode = True