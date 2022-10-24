from main import User, engine,Base

Base.metadata.create_all(engine) #create dabase with specified Base schema

#cmd: python create_db.py