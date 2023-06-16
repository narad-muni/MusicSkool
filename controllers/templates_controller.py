from flask import jsonify, redirect, url_for, render_template

def index_template(request, session):
    success = request.args.get('success')
    error = request.args.get('error')

    if(session.get("username")):
        return render_template('index.html', success=success, error=error)
    else:
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))
    
def login_template(request, session):
    if(session.get("username")):
        success = request.args.get('success')
        error = request.args.get('error')
        return render_template('index.html', success=success, error=error)
    else:
        success = request.args.get('success')
        error = request.args.get('error')

        return render_template('login.html', success=success, error=error)