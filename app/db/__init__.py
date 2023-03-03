from os import getenv                                   # getenv() function is part of Python's built-in 'os' module

# imported functions from sqalchemy to create variables:
from sqlalchemy.ext.declarative import declarative_base # 'base' class variable helps us map the models to real MySQL tables.
from sqlalchemy import create_engine                    # 'engine': manages the overall connection to the database
from sqlalchemy.orm import sessionmaker                 # 'session' variable generates temporary connections for performing CRUD 
from dotenv import load_dotenv

load_dotenv() #bc we used a .env file to fake the enviro variable, need to first call from the python-dotenv module, in prodn', 'DB_URL will be a proper enviro variable

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()