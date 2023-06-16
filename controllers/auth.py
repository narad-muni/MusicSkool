from flask import jsonify, redirect, url_for

def login(request, session):
    try:
        username = request.args.get('username')
        password = request.args.get('password')

        print(request, request.args)

        if(username == 'admin' and password == 'password'):
            session["username"] = username
            return redirect(url_for('index_template', success="Logged In Successfully"))
        else:
            return redirect(url_for('login_template', error="Invalid Username or Password"))
    except:
        return redirect(url_for('login_template', error="Some error occured"))

def logout(request, session):
    pass

def get_user(request, session):
    pass