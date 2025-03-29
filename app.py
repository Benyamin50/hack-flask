from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'payload': 'success'})


@app.route('/user', methods=['POST'])
def get_user():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['DELETE'])
def get_delete():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['PUT'])
def update_user():
    return jsonify({'payload': 'success', 'error': False})


@app.route('/api/v1/users', methods=['GET'])
def get_usersApi():
    return jsonify({'payload': []})



@app.route('/api/v1/user', methods=['POST'])
def get_postApi():
     email = request.args.get('email')
     name = request.args.get('name')

     return jsonify({'payload': {
            'email': email,
            'name': name
        }})


@app.route('/api/v1/user/add', methods=['POST'])
def get_postApiAdd():
     email = request.form.get('email')
     name = request.form.get('name')
     id = request.form.get('id')


     return jsonify({'payload': {
            'email': email,
            'name': name,
            'id': id

        }})

@app.route('/api/v1/user/create', methods=['POST'])
def postCreate():

    user_data = request.get_json()

    response = {
        'payload': {
            'email': user_data['email'],
            'name': user_data['name'],
            'id': user_data['id']
        }
    }
    
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)