import sys
import os
import os.path
sys.path.append('./')
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,backref)
from sqlalchemy.ext.declarative import declarative_base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database/sqlite/app.sqlite3")
engine = create_engine('sqlite:///'+ db_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()
