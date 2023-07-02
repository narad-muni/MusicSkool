from flask import jsonify, redirect, url_for, render_template
from utils import db

def student_subjects(request, session):
    success = request.args.get('success')
    error = request.args.get('error')
    user = session.get("user")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    data = db.execute_query(f'''select s.id, s.name, instrument, teacher_id, u.username  from `subject` s join `user` u on u.id = s.teacher_id where role='teacher'
    and s.id in (
        select ss.subject_id from `student_subject` ss where ss.user_id = {user[0]}
    )
    ''')
    
    return render_template('student_subjects.html', success=success, error=error, data=data)

def student_attendance(request, session):
    user = session.get("user")
    subject_id = request.args.get('subject_id')
    subject = request.args.get('subject')
    success = request.args.get('success')
    error = request.args.get('error')

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    student_id = user[0]
    student = user[1]

    data2 = db.execute_query(f'''
        select `date`, status from `attendance` a
        where student_id = {student_id}
        and subject_id = {subject_id}
    ''')

    data = []

    for d in data2:
        data.append(
            {
                "date": str(d[0]),
                "classname": d[1]
            }
        )

    return render_template('admin_view_attendance.html', success=success, error=error, student=student, subject=subject, data=data)

def student_marks(request, session):
    success = request.args.get('success')
    error = request.args.get('error')
    user = session.get("user")

    if(not session.get("user")):
        return redirect(url_for('login_template', success=success, error="Please Login to continue"))

    data2 = db.execute_query(f'''
        select s.name, s.id, u.id, u.username, m.marks from `marks` m
        join `user` u on u.id = m.student_id
        join `subject` s on s.id = m.subject_id
        where m.student_id={user[0]}
    ''')
    
    data = {}
    total = 0

    for d in data2:
        if(d[0] in data):
            data[d[0]][1].append(
                [d[2], d[3], d[4]]
            )
            total += d[4]
        else:
            data[d[0]] = [
                d[1],
                [
                    [d[2], d[3], d[4]]
                ]
            ]
            total += d[4]

    return render_template('student_marks.html', success=success, error=error, data=data, total=total)