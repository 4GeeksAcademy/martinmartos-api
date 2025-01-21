from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print('Incom.....', request_body)
    todos.append(request_body)
    return jsonify (todos)

app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('la posicion es...', position)
    del todos (position)
    return jsonify (todos)

todos = [{"label": "my first task", "done": False}]

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
        