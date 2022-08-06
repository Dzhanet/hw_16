import json
from models import *
from config import db


def insert_data_user(input_data):
    """JSON -> dict"""

    for row in input_data:
        db.session.add(User(
            id=row.get("id"),
            first_name=row.get("first_name"),
            last_name=row.get("last_name"),
            age=row.get("age"),
            email=row.get("email"),
            role=row.get("role"),
            phone=row.get("phone")))

    db.session.commit()


def insert_data_order(input_data):
    """JSON -> dict"""

    for row in input_data:
        db.session.add(Order(
            id=row.get("id"),
            name=row.get("name"),
            description=row.get("description"),
            start_date=row.get("start_date"),
            end_date=row.get("end_date"),
            address=row.get("address"),
            price=row.get("price"),
            customer_id=row.get("customer_id"),
            executor_id=row.get("executor_id")))

    db.session.commit()

def insert_data_offer(input_data):
    """JSON -> dict"""

    for row in input_data:
        db.session.add(Offer(
            id=row.get("id"),
            order_id=row.get("order_id"),
            executor_id=row.get("executor_id")))

    db.session.commit()


def get_all_users():
    """получает всех пользователей"""

    result = []
    for item in User.query.all():
        result.append(item.to_dict())

    return result

def get_all_orders():
    """получает все заказы в виде словаря"""

    result = []
    for item in Order.query.all():
        result.append(item.to_dict())

    return result

def get_all_offers():
    """получает все предложения в виде словаря"""

    result = []
    for item in Offer.query.all():
        result.append(item.to_dict())

    return result

def init_db():
    db.drop_all()  # удаляем все таблицы
    db.create_all()  # создаем их заново и отправляем данные из файлов

    with open("data/user.json") as file:
        data = json.load(file)
        insert_data_user(data)

    with open("data/order.json", encoding='utf-8') as file:
        data = json.load(file)
        insert_data_order(data)

    with open("data/offer.json") as file:
        data = json.load(file)
        insert_data_offer(data)

