#pip install sqlalchemy - instalacja sqlalchemy
#my będziemy pracować z SQL lite
from sqlalchemy.orm import declarative_base #klasa bazowa do tworzenia struktur bazy
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import Column, String, DateTime, Integer #pobieramy funkcje umożliwiające tworzenie kolumny i typów danych
from datetime import datetime 
from sqlalchemy import create_engine 
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) #directory name of our current directory

connection_string="sqlite:///"+os.path.join(BASE_DIR, 'site.db') #location of database 

Base = declarative_base()

engine = create_engine(connection_string, echo = True) #echo shows sql commands

Session = sessionmaker()

"""
W schemacie base tworzymy następujący obiekt:
class User 
    id int
    username str
    email str
    date_created datetime
"""

class User(Base): #dziedziczy z klasy Base do tworzenia obiektów
    __tablename__='users' #nazwa tabeli
    id = Column(Integer(), primary_key = True) #atrybut - klucz pierwotny
    username = Column(String(25), nullable = False, unique = True) #kolumna string niepusta i unikalna
    email = Column(String(80), unique = True, nullable = False) #kolumna string niepusta i unikalna
    date_created = Column(DateTime(),default = datetime.utcnow) #data i czas, domyślnie utcnow()

    def __repr__(self): #string representation of object
        return f"<User {self.username} email {self.email}>"


new_user = User(id = 1, username = "Szymon", email = "sd76805@student.sgh.waw.pl")
print(new_user)

#from main import User
#User.__tablename__
#User.__table__  <- metadata
