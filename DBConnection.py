import mysql.connector

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.__init__()
        return cls.__instance

class Connection(Singleton):
    __conn = None

    def __init__(self):
        if not self.__conn:
            self.__conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="hw2"
            )

    def execute_query(self, query, values=None):
        cursor = self.__conn.cursor()
        cursor.execute(query, values)
        if cursor.description is not None:
            result = cursor.fetchall()
        else:
            result = None
        cursor.close()
        self.__conn.commit()
        return result

# c = Connection()
# review_text = "good, but not very goog"
# customer_name = "Ashley"
# customer_surname = "Garcia"
# query = "SELECT customerId FROM customer as c WHERE c.firstName = %s AND c.lastName = %s LIMIT 1"
# values = (customer_name, customer_surname)
# result = c.execute_query(query, values)
# print(result)
# if result:
#     customer_id = result[0][0]
#     query = f"INSERT INTO review (reviewText, customerId) VALUES (%s, %s)"
#     values = (review_text, customer_id)
#     result = c.execute_query(query, values)
#     print(result)
