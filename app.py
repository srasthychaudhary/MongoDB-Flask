from flask import Flask , request , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask("db-app")
##### Connecting with SQLite ##########
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\Dell\Desktop\python\mydb\data.sqlite'

db = SQLAlchemy(app)
class record(db.Model):
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    city = db.Column(db.Text)
    id = db.Column(db.Integer , primary_key=True)

    def __init__(self,n,a,c):
        self.name = n
        self.age = a
        self.city = c
@app.route("/form_sqlite")
def myform():
    data = render_template("form_sqlite.html")
    return data

@app.route("/add_data_sqlite" )
def add_data_sqlite():
    n = request.args.get("name")
    a = request.args.get("age")
    c = request.args.get("city")
    
    db.create_all()
    obj = record(n ,a ,c)
    db.session.add(obj)
    db.session.commit()
    return "successful"

####### Connect with MongoDB #########

from pymongo import MongoClient
from ast import literal_eval
client = MongoClient('mongodb://127.0.0.1:27017')

@app.route('/mdbform')
def mdbform():
    data = render_template('mdbform.html')
    return data

@app.route('/add_data_mdb' , methods=['GET'])
def add_data_mdb():
    db_name = request.args.get('db_name')
    coll_name = request.args.get('coll_name')
    datadict = request.args.get('data')
    mydb = client[db_name]
    mycoll = mydb[coll_name]
    mycoll.insert(eval(datadict))
return "success"