from sqlalchemy.orm import Session
from . import models, schemas

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session, limit: int = 100):
    return db.query(models.Category).limit(limit).all()