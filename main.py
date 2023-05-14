from DBConnection import Connection
from flask import Flask, request, jsonify, make_response

app = Flask(__name__, static_url_path='/static/', static_folder='static')

container = Connection()


@app.route('/managing')
def manage():
    return app.send_static_file('managing.html')


@app.route('/serving')
def serve():
    return app.send_static_file('serving.html')


@app.route('/reviewing')
def review():
    return app.send_static_file('reviewing.html')


@app.route('/update_order', methods=['POST'])
def update_order():
    order_id = request.json['orderId']
    status = request.json['status']
    query = "SELECT * FROM hw2.order as o WHERE o.orderId = %s"
    values = (order_id, )
    result = container.execute_query(query, values)
    if result:
        query = "UPDATE hw2.order as o SET o.orderStatus = %s WHERE o.orderId = %s"
        values = (status, order_id)
        container.execute_query(query, values)
        return make_response(jsonify({'status': 'status updated'}), 202)
    else:
        return make_response(jsonify({'status': 'no such order'}), 202)


@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer_name = request.json['customerName']
    customer_surname = request.json['customerSurname']
    shiftTeamId = request.json['shiftTeamId']
    query = "SELECT customerId FROM customer WHERE firstName = %s AND lastName = %s"
    values = (customer_name, customer_surname)
    result = container.execute_query(query, values)
    if result:
        return make_response(jsonify({'status': 'customer already in the system'}), 202)
    else:
        query = "INSERT INTO customer (firstName, lastName, shiftTeamId) VALUES (%s, %s, %s)"
        values = (customer_name, customer_surname, shiftTeamId)
        container.execute_query(query, values)
        return make_response(jsonify({'status': 'customer added'}), 202)


@app.route('/submit_review', methods=['POST'])
def add_review():
    review_text = request.json['reviewText']
    customer_name = request.json['customerName']
    customer_surname = request.json['customerSurname']
    query = "SELECT customerId FROM customer WHERE firstName = %s AND lastName = %s"
    values = (customer_name, customer_surname)
    result = container.execute_query(query, values)
    if result:
        customer_id = result[0][0]
        query = "INSERT INTO review (reviewText, customerId) VALUES (%s, %s)"
        values = (review_text, customer_id)
        container.execute_query(query, values)
        return make_response(jsonify({'status': 'review added'}), 202)
    else:
        return make_response(jsonify({'status': 'no such customer'}), 202)


@app.route('/delete_review', methods=['POST'])
def delete_review():
    customer_name = request.json['customerName']
    customer_surname = request.json['customerSurname']
    query = "SELECT customerId FROM customer WHERE firstName = %s AND lastName = %s"
    values = (customer_name, customer_surname)
    result = container.execute_query(query, values)
    if result:
        customer_id = result[0][0]
        query = "DELETE FROM hw2.review WHERE customerId = %s;"
        values = (customer_id, )
        container.execute_query(query, values)
        return make_response(jsonify({'status': 'reviews deleted'}), 202)
    else:
        return make_response(jsonify({'status': 'no such customer'}), 202)


@app.route('/find_review', methods=['POST'])
def find_review():
    customer_name = request.json['customerName']
    customer_surname = request.json['customerSurname']
    print(customer_name)
    print(customer_surname)
    query = "SELECT customerId FROM customer WHERE firstName = %s AND lastName = %s"
    values = (customer_name, customer_surname)
    result = container.execute_query(query, values)
    print(result)
    if result:
        customer_id = result[0][0]
        query = "SELECT reviewText FROM review WHERE customerId = %s"
        values = (customer_id, )
        result = container.execute_query(query, values)
        if result:
            return make_response(jsonify({'status': result[0][0]}), 202)
        return make_response(jsonify({'status': "user hasn't reviews"}), 202)
    else:
        return make_response(jsonify({'status': 'no such customer'}), 202)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
