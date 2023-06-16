from flask import Flask, session, request, render_template, jsonify, redirect, url_for
from controllers import auth
from utils import migrate

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index_template():
    success = request.args.get('success')
    error = request.args.get('error')
    
    return render_template('index.html', success=success, error=error)

@app.route('/login')
def login_template():
    success = request.args.get('success')
    error = request.args.get('error')

    return render_template('login.html', success=success, error=error)

@app.route('/login_action')
def login_action():
    return auth.login(request, session)


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

@app.route('/poppulate')
def poppulate():
    try:
        migrate.poppulate()
        return redirect(url_for('index_template', success='John'))
    except:
        return redirect(url_for('index_template', error=30))        

if __name__ == '__main__':
    try:
        migrate.init()
        app.run()
    except Exception as e:
        print("Server failed to start : ",e)
