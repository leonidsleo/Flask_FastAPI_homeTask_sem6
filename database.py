import databases
import sqlalchemy

import settings

# DATABASE = "sqlite:///indatabase.db"
DATABASE_URL = settings.settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

# Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(100)),
    sqlalchemy.Column('description', sqlalchemy.String(500)),
    sqlalchemy.Column('price', sqlalchemy.Float),
)


# users - id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(50)),
    sqlalchemy.Column('lastname', sqlalchemy.String(50)),
    sqlalchemy.Column('email', sqlalchemy.String(150)),
    sqlalchemy.Column('password', sqlalchemy.String(200)),
)


# Таблица заказов : id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.


orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('produkt_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column('data', sqlalchemy.String),
    sqlalchemy.Column('status', sqlalchemy.String(30)),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

metadata.create_all(engine)