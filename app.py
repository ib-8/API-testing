from flask import Flask
from flask import jsonify
from flask import request
from flask_restful import Resource, Api

app=Flask(__name__)
api = Api(app)

class Hello(Resource):
    # def get(self):
    #     return jsonify({
    #         'message':'Hello World',
    #     })

    def post(self):
        data= request.get_json()
        return jsonify({
            'data':data,
        })

class Square(Resource):
    def get(self,num):
        return jsonify({
            'square':num**2,
        })

api.add_resource(Hello,'/')
api.add_resource(Square,'/square/<int:num>')

# @app.route('/<int:number>')
# def increment(number):
#     return jsonify(list(range(5)))

# @app.route('/<string:name>')
# def hello(name):
#     return jsonify({
#         'name':'jmit',
#         'address':'US',
#     })

if __name__ == '__main__':
    app.run(debug=True)