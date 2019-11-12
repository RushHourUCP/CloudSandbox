from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'info': 'Welcome to our REST API !'}

class Square(Resource):
    def get(self, num):
        return {'result': num*num}

class Route(Resource):
    def __init__(self):
        super().__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('starting_point', type=str)
        self.parser.add_argument('destination', type=str)

    def get(self):
        args = self.parser.parse_args()
        return {'Route': [args['starting_point'], args['destination']]}

api.add_resource(HelloWorld, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Route, '/route')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')