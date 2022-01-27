from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#postgresql://<username>:<password>@<ip-address/hostname>:<port_number>/<database_name>
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Mattia92@localhost:5432/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)  #it estabilished a connection to the BD

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#dependency
def get_db():           #get a session to the DB
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
### POSTGRESQL CONNECTION ###
while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database='fastapi',
                                user='postgres', password='Mattia92', cursor_factory=RealDictCursor)
        cursor = conn.cursor()  #this is what will execute SQL statements
        print("Database Connection was successfull!")
        break

    except Exception as error:
        print("Connecting to database Failed")
        print("Error: ", error)
        time.sleep(2)
### END ###
"""