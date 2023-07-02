from flask import jsonify, redirect, url_for, render_template
from utils import db

def teacher_attendance(request, session):
    success = request.args.get('success')
    error = request.args.get('error')
    user = session.get("user")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    data2 = db.execute_query(f'''
        select s.name, s.id, u.username, u.id from `student_subject` ss
        join `user` u on u.id = ss.user_id
        join `subject` s on s.id = ss.subject_id
        where u.role = 'student'
        and s.teacher_id = {user[0]}
    ''')
    
    data = {}
    for d in data2:
        if(d[0] in data):
            data[d[0]][1].append(
                [d[2],d[3]]
            )
        else:
            data[d[0]] = [
                d[1],
                [
                    [d[2], d[3]]
                ]
            ]

    return render_template('teacher_attendance.html', success=success, error=error, data=data)

def teacher_marks(request, session):
    success = request.args.get('success')
    error = request.args.get('error')
    user = session.get("user")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    data2 = db.execute_query(f'''
        select s.name, s.id, u.id, u.username, m.marks from `marks` m
        join `user` u on u.id = m.student_id
        join `subject` s on s.id = m.subject_id
        where s.teacher_id = {user[0]}
    ''')
    
    data = {}
    for d in data2:
        if(d[0] in data):
            data[d[0]][1].append(
                [d[2], d[3], d[4]]
            )
        else:
            data[d[0]] = [
                d[1],
                [
                    [d[2], d[3], d[4]]
                ]
            ]

    return render_template('teacher_marks.html', success=success, error=error, data=data)

def teacher_subjects(request, session):
    success = request.args.get('success')
    error = request.args.get('error')
    user = session.get("user")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    data = db.execute_query(f'''
        select s.id, s.name, instrument, teacher_id, u.username 
        from `subject` s
        join `user` u on u.id = s.teacher_id 
        where role='teacher' and s.teacher_id={user[0]}
    ''')
    
    return render_template('teacher_subjects.html', success=success, error=error, data=data)