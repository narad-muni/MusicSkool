from flask import Flask, session, request, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    username = data.get('username')
    password = data.get('password')

    # Perform authentication logic here
    # For simplicity, we're using a hardcoded username and password
    if username == 'admin' and password == 'password':
        session['username'] = username
        return jsonify({'message': 'Logged in successfully'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return jsonify({'username': username})
    else:
        return jsonify({'message': 'Unauthorized'}), 401


@app.route('/logout')
def logout():
    session.pop('username', None)
    return jsonify({'message': 'Logged out successfully'})


if __name__ == '__main__':
    app.run()
