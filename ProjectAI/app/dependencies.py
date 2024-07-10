from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "sqlite:///./test.db"  # замените на вашу базу данных

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = Database(DATABASE_URL)
