from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import product
from database import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"]
)

# Create tables
database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "Welcome"}

# Sample data
products = [
    product(id=1, name="VIVO", description="Budget friendly phone", price=9999, quantity=20),
    product(id=2, name="ASUS", description="Gaming Laptop", price=55555, quantity=10),
    product(id=3, name="BOAT", description="High quality bluetooth", price=777, quantity=5)
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = SessionLocal()
    count = db.query(database_models.product).count()
    if count == 0:
        for prod in products:
            db.add(database_models.product(**prod.model_dump()))
        db.commit()
    db.close()

init_db()

# Get all products
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.product).all()
    return db_products

# Get product by ID
@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.product).filter(database_models.product.id == id).first()
    if db_product:
        return db_product
    return {"message": "Product not found"}

# Add a product (✅ Fixed)
@app.post("/products", response_model=product)
def add_product(prod: product, db: Session = Depends(get_db)):
    new_product = database_models.product(**prod.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put("/products/{id}")
def update_product(id: int, product: product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.product).filter(database_models.product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        db.refresh(db_product)
        return {"message": "Product updated successfully"}
    else:
        return {"message": "No product found"}


# Delete a product
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.product).filter(database_models.product.id == id).first()
    if not db_product:
        return {"message": "No product found"}
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}
