#if not used the pydantic will sya it is not my syntax and error will be occured

from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

class product(Base):#must inherit

    __tablename__= "products"
    id= Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)