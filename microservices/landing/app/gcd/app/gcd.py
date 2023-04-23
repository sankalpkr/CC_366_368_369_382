from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class gcd(Resource):
    def get(self,x,y):
    	return computeGCD(int(x),int(y))
    


def computeGCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd

api.add_resource(gcd,'/gcd/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5060)
