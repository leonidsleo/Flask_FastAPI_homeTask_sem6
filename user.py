from fastapi import APIRouter
from random import randint

import database as db
import models as m
import datetime


router = APIRouter()

# @router.get('/')
# def root():
#     return 'ПРИВЕТ'

# заполняем таблицы для примера
@router.get('/add_proba_user/{count}')
async def add_proba_user(count: int):
    for i in range(count):
        query = db.users.insert().values(name=f'user{i}', lastname=f'lastname{i}', email=f'mail.user{i}@mail.ru', password=f'password{i}')
        await db.database.execute(query)
    return {'сообщение': f'{count} пользователей добавлено'}


@router.get('/add_proba_product/{count}')
async def add_proba_product(count: int):
    for i in range(count):
        query = db.products.insert().values(name=f'product{i}', description=f'продукт{i} хороший', price=randint(300, 10500))
        await db.database.execute(query)
    return {'сообщение': f'{count} продуктов добавлено'}


@router.get('/add_proba_order/{count}')
async def add_proba_order(count: int):
    for i in range(count):
        query = db.orders.insert().values(user_id=randint(1, 10), produkt_id = randint(1, 10), data=datetime.datetime.now(), status='new')
        await db.database.execute(query)
    return {'сообщение': f'{count} заказов добавлено'}


@router.post('/user/', response_model=m.User)
async def add_user(user: m.AddUser):
    query = db.users.insert().values(**user.dict())
    last_record_id = await db.database.execute(query)
    return {**user.dict(), 'id': last_record_id}


@router.post('/produkt/', response_model=m.Product)
async def add_product(produkt: m.AddProduct):
    query = db.products.insert().values(**produkt.dict())
    last_record_id = await db.database.execute(query)
    return {**produkt.dict(), 'id': last_record_id}


@router.post('/order/', response_model=m.Order)
async def add_order(order: m.AddOrder):
    query = db.orders.insert().values(**order.dict())
    last_record_id = await db.database.execute(query)
    return {**order.dict(), 'id': last_record_id}


@router.get('/user/', response_model=list[m.User])
async def all_user():
    query = db.users.select()
    return await db.database.fetch_all(query)


@router.get('/product/', response_model=list[m.Product])
async def all_product():
    query = db.products.select()
    return await db.database.fetch_all(query)


@router.get('/order/', response_model=list[m.Order])
async def all_order():
    query = db.orders.select()
    return await db.database.fetch_all(query)


@router.get('/user/{user_id}', response_model=m.User)
async def search_user(user_id: int):
    query = db.users.select().where(db.users.c.id == user_id)
    return await db.database.fetch_one(query)


@router.get('/product/{product_id}', response_model=m.Product)
async def search_product(product_id: int):
    query = db.products.select().where(db.products.c.id == product_id)
    return await db.database.fetch_one(query)


@router.get('/order/{order_id}', response_model=m.Order)
async def search_order(order_id: int):
    query = db.orders.select().where(db.orders.c.id == order_id)
    return await db.database.fetch_one(query)


@router.put('/user/{user_id}', response_model=m.User)
async def update_user(user_id: int, new_user: m.AddUser):
    query = db.users.update().where(db.users.c.id == user_id).values(**new_user.dict())
    await db.database.execute(query)
    return {**new_user.dict(), 'id': user_id}


@router.put('/product/{product_id}', response_model=m.Product)
async def update_product(product_id: int, new_product: m.AddProduct):
    query = db.products.update().where(product_id == db.products.c.id).values(**new_product.dict())
    await db.database.execute(query)
    return {**new_product.dict(), 'id': product_id}


@router.put('/order/{order_id}', response_model=m.Order)
async def update_order(order_id: int, new_order: m.AddOrder):
    query = db.orders.update().where(order_id == db.orders.c.id).values(**new_order.dict())
    await db.database.execute(query)
    return {**new_order.dict(), 'id': order_id}


@router.delete('/user/{user_id}')
async def delete_user(user_id: int):
    query = db.users.delete().where(db.users.c.id == user_id)
    await db.database.execute(query)
    return {'сообщение': 'Пользователь удален'}


@router.delete('/product/{product_id}')
async def delete_product(product_id: int):
    query = db.products.delete().where(db.products.c.id == product_id)
    await db.database.execute(query)
    return {'сообщение': 'Товар удален'}


@router.delete('/order/{order_id}')
async def delete_order(order_id: int):
    query = db.orders.delete().where(db.orders.c.id == order_id)
    await db.database.execute(query)
    return {'сообщение': 'Заказ удален'}