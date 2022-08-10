import json
from config import app
from models import User, Order, Offer
from service import get_all_users, get_all_orders, get_all_offers, init_db, insert_data_user, update_universal, \
    insert_data_order, insert_data_offer, delete_universal
from flask import request


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return json.dumps(get_all_users()), 200
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user(request.json)
        else:
            print('Непонятный типа данных')

@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_users(user_id):
    if request.method == 'GET':
        data = get_all_users()
        for item in data:
            if item.get("id") == user_id:
                return json.dumps(item), 200

    elif request.method == 'PUT':
        update_universal(User, user_id, request.json)

    elif request.method == 'DELETE':
        delete_universal(User, user_id)

    return 'Не знаю такого пользователя, у меня лапки'

@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return json.dumps(get_all_orders(),ensure_ascii=False), 200
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order(request.json)

@app.route("/orders/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_order(user_id):
    if request.method == 'GET':
        data = get_all_orders()
        for item in data:
            if item.get("id") == user_id:
                return json.dumps(item,ensure_ascii=False), 200

    elif request.method == 'PUT':
        update_universal(Order, user_id, request.json)

    elif request.method == 'DELETE':
        delete_universal(Order, user_id)

    return 'Не вижу такой заказ, у меня лапки'

@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return json.dumps(get_all_offers(),ensure_ascii=False), 200
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer(request.json)

@app.route("/offers/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_offer(user_id):
    if request.method == 'GET':
        data = get_all_offers()
        for item in data:
            if item.get("id") == user_id:
                return json.dumps(item), 200
    elif request.method == 'PUT':
        update_universal(Offer, user_id, request.json)

    elif request.method == 'DELETE':
        delete_universal(Offer, user_id)

    return 'Не вижу предложение, у меня лапки'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
