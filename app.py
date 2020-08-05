from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth
import logging
auth = HTTPBasicAuth()

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('You can add a message to the log')
logging.info('So should log all your requests')
logging.warning('This is a warning')
logging.error('This is an error, **chokes**')

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Learn Python',
        'description': 'A clever way to learn Python is to start with the basics',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Flask',
        'description': 'Flask is one awesome package that is un-opinonated',
        'done': False
    },
    {
        'id': 3,
        'title': 'Learn Databases',
        'description': 'Understand sql and NoSql databases and difference between a releational and document based database',
        'done': True
    }
]


@auth.get_password
def get_password(username):
    if username == 'ahad':
        return 'bokhari'
    return None


@app.route('/', methods=['GET'])
@auth.login_required
def get_index():
    return jsonify(hello='world'), 200


@app.route('/todo/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks}), 200


@app.route('/todo/tasks', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]}), 200


@app.route('/todo/tasks/<int:task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
