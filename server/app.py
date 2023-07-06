import os
import psycopg2
from flask import Flask
from flask_restful import Resource
from flask import make_response
from config import  api, app, db


# # conn = psycopg2.connect(
# #         host="localhost",
# #         url = os.environ.get("DATABASE_URL"),
# #         user = os.environ.get('DB_USERNAME'),
# #         password= os.environ.get('DB_PASSWORD')
# #         )


class Home(Resource):
    def get(self):
        return make_response("HOWDY")
    
api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(port=5554, debug=True)