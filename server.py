import os
import jwt
import datetime
from flask import Flask, request
from dotenv import load_dotenv
from flask_mysqldb import MySQL
load_dotenv()

server = Flask(__name__)

mysql = MySQL(server)

server.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
server.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
server.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
server.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
server.config['MYSQL_PORT'] = os.environ.get('MYSQL_PORT')
# print(server.config['MYSQL_HOST'], os.environ.get('MYSQL_USER'))

@server.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    # check db for authorization
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password from USER where email=%s", (auth.username)
    )
    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if auth.username != email or auth.password != password:
            return "Invalid Credentials", 401

        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
    else:
        return "Invalid credentials", 401



def createJWT(username, secret, authz):
    return jwt.encode({
        "username": username,
        "exp": datetime.datetime.now(tz=datetime.timezone.utc)+ datetime.timedelta(days=+1),
        "iat": datetime.datetime.now(),
        "admin": authz
        }, secret,
        algorithm="HS256"
    )

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)