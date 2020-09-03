from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import os
import bcrypt
#venv\Scripts\activate
#$env:FLASK_APP='app.py'
#$env:API_KEY='x{lhtTaQz58QJ7ZK;a~`/t!:D'
#env:DATABASE_URI='postgres://hvlgtapyoydbfe:2dd3f2b94636564113e114a2f68862631ea02ac1e835ee4e45f0668230b5f9dc@ec2-184-72-235-159.compute-1.amazonaws.com:5432/d9ca62s6qk8gl8'

app = Flask(__name__)
DATABASE_URI = os.environ["DATABASE_URI"]
API_KEY = os.environ["API_KEY"]
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.id}')"
        
def check_api_key(sent_key):
    if sent_key == API_KEY:
        return True
    else:
        return False

@app.route("/api/login", methods=["POST"])
def login():
    sent_key = request.json.get("api_key", None)
    if not check_api_key(sent_key):
        return jsonify({"status_code": 401})
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #if bcrypt.checkpw(password.encode('utf-8'), hashed):
    return jsonify({"status_code": 200, "hashed": hashed.decode('utf-8')})

if __name__ == '__name__':
    app.run(debug=True)
