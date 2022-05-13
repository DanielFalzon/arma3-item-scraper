from . import models, schemas, crud
from .database import engine

models.Base.metadata.create_all(bind=engine)