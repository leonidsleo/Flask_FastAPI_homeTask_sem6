from pydantic import BaseModel, Field
from datetime import datetime 


class AddProduct(BaseModel):
    name: str = Field(max_length=100)
    description: str = Field(max_length=500)
    price: float = Field(default=0.00)


# class Product(BaseModel):
#     id: int
#     name: str = Field(max_length=100)
#     description: str = Field(max_length=500)
#     price: float = Field(default=0.00)


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float



class AddUser(BaseModel):
    name: str = Field(max_length=50)
    lastname: str = Field(max_length=50)
    email: str = Field(max_length=150)
    password: str = Field(max_length=200)


# class User(BaseModel):
#     id: int
#     name: str = Field(max_length=50)
#     lastname: str = Field(max_length=50)
#     email: str = Field(max_length=150)
#     password: str = Field(max_length=200)


class User(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    password: str


class AddOrder(BaseModel):
    user_id: int
    produkt_id: int
    data: datetime = Field(default=datetime.now())
    status: str = Field(default='New')


class Order(BaseModel):
    user_id: int
    produkt_id: int
    data: datetime
    status: str