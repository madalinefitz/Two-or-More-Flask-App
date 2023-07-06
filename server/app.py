import os
import psycopg2
from flask import Flask
from flask_restful import Resource
from flask import make_response
from config import  api, app
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy



load_dotenv() 

# conn = psycopg2.connect(
#         host="localhost",
#         url = os.environ.get("DATABASE_URL"),
#         user = os.environ.get('DB_USERNAME'),
#         password= os.environ.get('DB_PASSWORD')
#         )


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
# DB_URL = "jdbc:postgresql://lin-12158-3411-pgsql-primary.servers.linodedb.net:5432/postgres"

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)

# # Open a cursor to perform database operations
# cur = conn.cursor()

# # # Execute a command: this creates a new table
# # cur.execute('DROP TABLE IF EXISTS books;')
# # cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
# #                                  'title varchar (150) NOT NULL,'
# #                                  'author varchar (50) NOT NULL,'
# #                                  'pages_num integer NOT NULL,'
# #                                  'review text,'
# #                                  'date_added date DEFAULT CURRENT_TIMESTAMP);'
# #                                  )

# # # Insert data into the table

# # cur.execute('INSERT INTO books (title, author, pages_num, review)'
# #             'VALUES (%s, %s, %s, %s)',
# #             ('A Tale of Two Cities',
# #              'Charles Dickens',
# #              489,
# #              'A great classic!')
# #             )


# # cur.execute('INSERT INTO books (title, author, pages_num, review)'
# #             'VALUES (%s, %s, %s, %s)',
# #             ('Anna Karenina',
# #              'Leo Tolstoy',
# #              864,
# #              'Another great classic!')
# #             )

# conn.commit()

# cur.close()
# conn.close()

class Home(Resource):
    def get(self):
        return make_response("HOWDY")
    
api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(port=5554, debug=True)