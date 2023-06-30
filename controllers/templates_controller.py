from flask import jsonify, redirect, url_for, render_template
from utils import db

def index_template(request, session):
    success = request.args.get('success')
    error = request.args.get('error')

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))
    
    return user_main_template(request, session)
        

def user_main_template(request, session):
    request.args = request.args.copy()

    request.args["success"] = "Logged In Successfully"

    if(session.get("user")[3] == "admin"):
        return redirect(url_for('admin_subjects'))
    # elif(session.get("user")[3] == "teacher"):
    #     return render_template('teacher_subjects.html', success=success, error=error)
    # else:
    #     return render_template('student_subjects.html', success=success, error=error)
    
def admin_subjects(request, session):
    success = request.args.get('success')
    error = request.args.get('error')

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    data = db.execute_query("select s.id, s.name, instrument, teacher_id, u.username  from `subject` s join `user` u on u.id = s.teacher_id where role='teacher'")
    
    return render_template('admin_subjects.html', success=success, error=error, data=data)

def admin_students(request, session):
    success = request.args.get('success')
    error = request.args.get('error')

    data = db.execute_query("select * from `user` where role='student'")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))
    
    return render_template('admin_students.html', success=success, error=error, data=data)

def admin_teachers(request, session):
    success = request.args.get('success')
    error = request.args.get('error')

    data = db.execute_query("select * from `user` where role='teacher'")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))
    
    return render_template('admin_teachers.html', success=success, error=error, data=data)

def admin_create_subjects(request, session):
    success = request.args.get('success')
    error = request.args.get('error')

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    data = db.execute_query("select id, username  from `user` u where role='teacher'")
    
    return render_template('admin_create_subjects.html', success=success, error=error, data=data)

def admin_edit_subjects(request, session):
    success = request.args.get('success')
    error = request.args.get('error')
    id = request.args.get("id")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    teachers = db.execute_query("select id, username  from `user` u where role='teacher'")

    data = db.execute_query(f"select id, name, instrument, teacher_id  from `subject` u where id={id}")[0]
    
    return render_template('admin_edit_subjects.html', success=success, error=error, data=data, teachers=teachers)

def admin_create_users(request, session):
    success = request.args.get('success')
    error = request.args.get('error')
    role = request.args.get('role')

    if(not session.get("user")):
        return redirect(url_for('admin_create_users', success=success, error="Please Login to continue"))
    
    return render_template('admin_create_users.html', success=success, error=error, role=role)


def admin_edit_users(request, session):
    success = request.args.get('success')
    error = request.args.get('error')
    id = request.args.get("id")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    data = db.execute_query(f"select id, username, password, role  from `user` u where id={id}")[0]
    subjects = db.execute_query(f"select id, name  from `subject`")
    selected_subjects = db.execute_query(f"select ss.id, s.name, s.id  from `student_subject` ss join `subject` s on s.id = ss.subject_id where ss.user_id = {id}")
    selected_subjects_arr = [s[2] for s in selected_subjects]

    return render_template('admin_edit_users.html', success=success, error=error, data=data, selected_subjects_arr=selected_subjects_arr, subjects=subjects, selected_subjects=selected_subjects)

def login_template(request, session):
    if(session.get("user")):
        success = request.args.get('success')
        error = request.args.get('error')

        return render_template('index.html', success=success, error=error)
    else:
        success = request.args.get('success')
        error = request.args.get('error')

        return render_template('login.html', success=success, error=error)