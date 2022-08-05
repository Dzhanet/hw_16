import json
from config import app
from service import get_all_users, get_all_orders



@app.route("/users/", methods=['GET'])
def get_users():
    return json.dumps(get_all_users()), 200

@app.route("/users/<int:user_id>", methods=['GET'])
def get_one_users(user_id):
    data = get_all_users()
    for item in data:
        if item.get("id") == user_id:
            return json.dumps(item), 200

    return 'Не знаю такого пользователя, у меня лапки'

@app.route("/orders/", methods=['GET'])
def get_orders():
    return json.dumps(get_all_orders()), 200

@app.route("/orders/<int:order_id>", methods=['GET'])
def get_one_order(order_id):
    data = get_all_orders()
    for item in data:
        if item.get("id") == order_id:
            return json.dumps(item), 200

    return 'Не вижу такой заказ, у меня лапки'



if __name__ == '__main__':
    app.run(debug=True)
