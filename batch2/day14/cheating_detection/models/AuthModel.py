from lib.db import *

class AuthModel:

    def __init__(self):
        self.conn = connect("app.db")

    def getUser(self,username,password):
        query = f"SELECT * FROM users WHERE username='{username}' and password='{password}' "
        result = fetchone(self.conn,query)
        print(result)
        return result

    def createUser(self,name,phone,email,username,password,role):
        query = f"INSERT INTO users (name,phone,email,username,password,role)" \
                f" VALUES ('{name}',{phone},'{email}','{username}','{password}','{role}')"
        try:
            insert(self.conn,query)
            print("The record is inserted")
            result = 1
        except:
            print('Error in inserting into database')
            result = 0
        return result

if __name__ == '__main__':
    am = AuthModel()

