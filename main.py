from flask import Flask, session, request, render_template, jsonify, redirect, url_for
from controllers import auth, templates_controller
from utils import migrate

# Config

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Templates

@app.route('/')
def index_template():
    return templates_controller.index_template(request, session)

@app.route('/login')
def login_template():
    return templates_controller.login_template(request, session)

# Actions

@app.route('/login_action')
def login_action():
    return auth.login(request, session)

@app.route('/logout_action')
def logout():
    session.pop('username', None)

    request.args = request.args.copy()

    request.args["success"] = "Logged out successfully"
    return templates_controller.login_template(request, session)

# Custom Endpoints

@app.route('/poppulate')
def poppulate():
    request.args = request.args.copy()

    try:
        migrate.poppulate()
        request.args["success"] = "Poppulating DB Successful"
    except:
        request.args["error"] = "Poppulating DB Failed"

    return templates_controller.index_template(request, session)

if __name__ == '__main__':
    try:
        migrate.init()
        app.run()
    except Exception as e:
        print("Server failed to start : ",e)
