from flask import Flask, jsonify, request
import  manaliz
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/get-data', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/set-data', methods=['POST'])
def addOne():
    mas = manaliz.analiz(request.get_json())
    # print(mas)
    return jsonify(mas)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
