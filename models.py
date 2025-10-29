from pydantic import BaseModel

class product(BaseModel):#must inherit
    id: int
    name:str
    description:str
    price: float
    quantity:int

#create a constructor class to call it in another file
"""   def __init__(self,id:int,name:str,description:str,price:float,quantity:int):
        self.id=id
        self.name=name
        self.description=description
        self.price=price
        self.quantity=quantity"""
