from dotenv import dotenv_values
from sqlalchemy import create_engine

url = dotenv_values('.env')['DATABASEURL']
engine = create_engine(url, echo=True)

# session

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Model

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'

Base.metadata.create_all(engine)

# Create new

user = User(name='John Snow', password='johnspassword')
session.add(user)

print(user.id)  # None

# Search

query = session.query(User).filter_by(name='John')

query.count()

session.query(User).filter(User.name=='John').first()

session.query(User).filter(User.name.like('%John%')).first()
