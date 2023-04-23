from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class lt(Resource):
    def get(self,x,y):
    	return x<y

api.add_resource(lt,'/lt/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5062)
