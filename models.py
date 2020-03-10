from database import *

class Key(Base):
    __tablename__ = 'key'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    created_at = Column(DateTime)