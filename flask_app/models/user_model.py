#model file contains constructor and methods for class
#constructor takes results from query and turns it into python objects

from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f"< first name: {self.first_name}, id:{self.id}>"

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for row in results:
            users.append(User(row))
        return users

    @classmethod
    def add_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s, %(email)s)"
        result = connectToMySQL('users_schema').query_db(query,data)
        return result