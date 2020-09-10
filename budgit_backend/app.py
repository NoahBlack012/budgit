#Get rid of uuid for item
from flask import Flask, request, jsonify, session, make_response
from flask_cors import CORS
import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import os
import bcrypt
#venv\Scripts\activate
#$env:FLASK_APP='app.py'
#$env:API_KEY='x{lhtTaQz58QJ7ZK;a~`/t!:D'
#env:DATABASE_URI='postgres://hvlgtapyoydbfe:2dd3f2b94636564113e114a2f68862631ea02ac1e835ee4e45f0668230b5f9dc@ec2-184-72-235-159.compute-1.amazonaws.com:5432/d9ca62s6qk8gl8'

app = Flask(__name__)
CORS(app)
DATABASE_URI = os.environ["DATABASE_URI"]
API_KEY = os.environ["API_KEY"]
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    categories = db.Column(db.ARRAY(db.String), nullable=False, default=["food", "transportation", "shopping", "rent"])

    def __repr__(self):
        return f"User('{self.username}', '{self.password}', '{self.id}', '{self.categories}')"

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    userid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    value = db.Column(db.Numeric, nullable=False)
    category = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Item('{self.id}', '{self.userid}', '{self.title}', '{self.value}', '{self.category}')"

def check_api_key(sent_key):
    if sent_key == API_KEY:
        return True
    else:
        return False


@app.route("/api/signup", methods=["POST"])
def signup():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    db_users = User.query.filter_by(username=username)
    for user in db_users:
        if user.username == username:
            return jsonify({"user_created": False})
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, password=hashed_password.decode('utf-8'))
    db.session.add(new_user)
    db.session.commit()
    id = User.query.filter_by(username=username).first().id
    return jsonify({"user_created": True, "id": id})

@app.route("/api/login", methods=["POST"])
def login():
    sent_key = request.json.get("api_key", None)
    if not check_api_key(sent_key):
        return jsonify({"status_code": 401})
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    #hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db_user = User.query.filter_by(username=username).first()
    db_password = db_user.password
    if bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
        return jsonify({"status_code": 200, "userid": db_user.id, "login": True})
    else:
        return jsonify({"status_code": 200, "login": False})

@app.route("/api/get_items", methods=["POST"])#@login_required
def get_items():
    userid = request.json.get("userid", None)
    sent_key = request.json.get("api_key", None)
    if not check_api_key(sent_key):
        return make_response(jsonify({"status_code": 401}), 401)
    items = Item.query.filter_by(userid=userid).all()
    json_items = []
    for item in items:
        json_items.append(
            {
                "id": item.id,
                "userid": item.userid,
                "title": item.title,
                "value": float(item.value),
                "category": item.category
            }
        )
    res = make_response(jsonify({"status_code": 200, "items": json_items}), 200)
    return res

@app.route("/api/add_item", methods=["POST"])
def add_item():
    userid = request.json.get("userid", None)
    sent_key = request.json.get("api_key", None)
    new_item = request.json.get("new_item", None)
    if not check_api_key(sent_key):
        return make_response(jsonify({"status_code": 401}), 401)

    #item = Item(userid=1, title="ABC", value=123, category="food")
    new_item_object = Item(
        userid=userid,
        title=new_item["title"],
        value=new_item["value"],
        category=new_item["category"]
    )
    db.session.add(new_item_object)
    db.session.commit()
    return make_response(jsonify({"status_code": 200, "id": new_item_object.id}), 200)

@app.route("/api/delete_item", methods=["POST"])
def delete_item():
    userid = request.json.get("userid", None)
    sent_key = request.json.get("api_key", None)
    deleted_id = request.json.get("deleted_id", None)
    if not check_api_key(sent_key):
        return make_response(jsonify({"status_code": 401}), 401)

    Item.query.filter_by(id=deleted_id).delete() #delete the item with the id provided from the db
    db.session.commit()
    return make_response(jsonify({"status_code": 200}), 200)

@app.route("/api/add_category", methods=["POST"])
def add_category():
    userid = request.json.get("userid", None)
    sent_key = request.json.get("api_key", None)
    new_category = request.json.get("new_category", None)
    if not check_api_key(sent_key):
        return make_response(jsonify({"status_code": 401}), 401)
    categories = User.query.filter_by(id=userid).first().categories
    categories.append(new_category)
    User.query.filter_by(id=userid).first().categories = categories
    db.session.commit()
    user_categories = User.query.filter_by(id=userid).first().categories
    print (user_categories)
    return make_response(jsonify({"status_code": 200, "categories": user_categories}), 200)

@app.route("/api/get_categories", methods=["POST"])
def get_categories():
    userid = request.json.get("userid", None)
    sent_key = request.json.get("api_key", None)
    if not check_api_key(sent_key):
        return make_response(jsonify({"status_code": 401}), 401)
    user_categories = User.query.filter_by(id=userid).first().categories
    return make_response(jsonify({"status_code": 200, "categories": user_categories}), 200)

if __name__ == '__name__':
    app.run(debug=True)
