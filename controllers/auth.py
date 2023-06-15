import json
from flask import jsonify
def login(request, session):
    try:
        username = request.form.get('username')
        password = request.form.get('password')


        return jsonify({"hi":"yo"}), 203
    except:
        pass

def logout(request, session):
    pass

def get_user(request, session):
    pass