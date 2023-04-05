from flask import Flask, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

tasks = {
    'lawn mowing': {'location': '123 Main St, Anytown, USA', 'cost': 50},
    'groceries': {'location': '456 Elm St, Anytown, USA', 'cost': 20},
    'fedex': {'location': '789 Oak St, Anytown, USA', 'cost': 10},
    'cleaning the car': {'location': '321 Maple St, Anytown, USA', 'cost': 30},
    'walking the dog': {'location': '654 Pine St, Anytown, USA', 'cost': 15},
    'watering plants': {'location': '987 Cedar St, Anytown, USA', 'cost': 25}
}

class Task(Resource):
    def get(self, task):
        if task not in tasks:
            return {'task': None, 'message': 'Task not found'}, 404
        return tasks[task]

class Location(Resource):
    def post(self):
        data = request.get_json()
        address = data['address']
        url = 'https://api.geocode.xyz'
        params = {'auth': '1234567890abcdefg', 'locate': address, 'json': 1}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            lat = response.json()['latt']
            lon = response.json()['longt']
            return {'latitude': lat, 'longitude': lon}
        else:
            return {'message': 'Unable to geocode address'}, 400

api.add_resource(Task, '/task/<string:task>')
api.add_resource(Location, '/location')

if __name__ == '__main__':
    app.run(debug=True)

