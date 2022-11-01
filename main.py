import psycopg2
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import create_tables, Stock, Shop, Publisher, Book

DSN = 'postgresql://postgres:64082@localhost:5432/ORM'
engine = sqlalchemy.create_engine(DSN)
#create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

name_publisher = input("Имя издателя: ")

subq = session.query(Publisher).filter(Publisher.name == name_publisher).subquery()
subq2 = session.query(Book).join(subq, Book.id_publisher == subq.c.id).subquery()
subq3 = session.query(Stock).join(subq2, Stock.id_book == subq2.c.id).subquery()
for c in session.query(Shop).join(subq3, Shop.id == subq3.c.id_shop).all():
    print(c)

session.close()

