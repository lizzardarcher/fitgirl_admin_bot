from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)
import sqlalchemy

engine=sqlalchemy.create_engine(f'sqlite:///{BASE_DIR}\\db.sqlite3', echo=True)

from sqlalchemy import select
from sqlalchemy.orm import Session
session = Session(engine)

from sqlalchemy import inspect
insp = inspect(engine)
