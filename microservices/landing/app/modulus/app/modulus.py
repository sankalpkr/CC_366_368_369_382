from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class modulus(Resource):
    def get(self,x,y):
    	return int(x)%int(y)

api.add_resource(modulus,'/modulus/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5059)
