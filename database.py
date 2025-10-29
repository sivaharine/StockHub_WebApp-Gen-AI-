from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url="postgresql://postgres:2912@localhost:5432/items"

engine=create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
