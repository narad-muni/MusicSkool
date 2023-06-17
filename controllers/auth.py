from flask import jsonify, redirect, url_for
from utils import db

def login(request, session):
    try:
        username = request.args.get('username', "")
        password = request.args.get('password', "")

        user = db.execute_query(f"select id, username, password, role from `user` where username = '{username}' and password = '{password}'")

        if(user):
            session["user"] = user[0]
            return redirect(url_for('index_template', success="Logged In Successfully"))
        else:
            return redirect(url_for('login_template', error="Invalid Username or Password"))
    except Exception as e:
        return redirect(url_for('login_template', error="Some error occured"))

def logout(request, session):
    session.pop('user', None)

    return redirect(url_for('login_template', success="Logged out successfully"))

def get_user(request, session):
    pass