from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
import json
import datetime
import os


db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS') 

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

def create_app(test_config=None):
    app = Flask(__name__)
    cors = CORS(app)

    print("database")
    #database configurations
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = db_user
    app.config['MYSQL_PASSWORD'] = db_password
    app.config['MYSQL_DB'] = 'grievancesDB'
    
    mysql = MySQL(app)
    
    #app configurations
    app.config["JSON_SORT_KEYS"] = False
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    #main route - gets back all grievances
    @app.route('/grievances')
    @cross_origin()
    def students():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM grievances")
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json.loads(json.dumps(json_data, default=default)))
    
    return app