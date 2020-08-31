from flask import Flask
from flask_restful import Api, Resource
#venv\Scripts\activate
#$env:FLASK_APP='app.py'
app = Flask(__name__)
api = Api(app)

class hi(Resource):
    def get(self):
        return {"msg": "Hi"}

api.add_resource(hi, "/hi")

if __name__ == '__name__':
    app.run(debug=True)