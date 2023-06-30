from flask import jsonify, redirect, url_for
from utils import db

def admin_delete_users_action(request, session):
    try:
        id = request.args.get('id', "")
        role = request.args.get('role', "")

        db.execute_query(f'''
            delete from `user` where id = {id}
        ''')

        db.execute_query(f'''
            delete from `student_subject` where user_id = {id}
        ''')

        return redirect(url_for(f'admin_{role}s', success=f"{role} deleted successfully"))
    except Exception as e:
        print(e)
        return redirect(url_for(f'admin_{role}s', error="some error occured"))

def admin_add_student_subject_action(request, session):
    try:
        user_id = request.args.get('user_id', "")
        subject_id = request.args.get('subject_id', "")

        db.execute_query(f'''
            insert into `student_subject`(subject_id, user_id)
            values({subject_id}, {user_id})
        ''')

        return redirect(url_for(f'admin_edit_users', id=user_id, success=f"subject added successfully"))
    except Exception as e:
        print(e)
        return redirect(url_for(f'admin_edit_users', id=user_id, error="some error occured"))

def admin_delete_student_subject_action(request, session):
    try:
        id = request.args.get('id', "")
        ss_id = request.args.get('ss_id', "")

        db.execute_query(f'''
            delete from `student_subject` where id = {ss_id}
        ''')

        return redirect(url_for('admin_edit_users', id=id, success="Subject deleted successfully"))
    except:
        return redirect(url_for('admin_edit_users', id=id, error="some error occured"))

def admin_create_subject_action(request, session):
    try:
        subject = request.args.get('subject', "")
        instrument = request.args.get('instrument', "")
        teacher = request.args.get('teacher', 0)

        db.execute_query(f'''
            insert into `subject`(name, instrument, teacher_id) values('{subject}', '{instrument}', '{teacher}')
        ''')

        return redirect(url_for('admin_subjects', success="Subject created successfully"))
    except Exception as e:
        print(e)
        return redirect(url_for('admin_subjects', error="some error occured"))

def admin_edit_subject_action(request, session):
    try:
        id = request.args.get('id', "")
        subject = request.args.get('subject', "")
        instrument = request.args.get('instrument', "")
        teacher = request.args.get('teacher', 0)

        db.execute_query(f'''
            update `subject`
            set name = '{subject}',
            instrument = '{instrument}',
            teacher_id = '{teacher}'
            where id = '{id}'
        ''')

        return redirect(url_for('admin_subjects', success="Subject edited successfully"))
    except Exception as e:
        print(e)
        return redirect(url_for('admin_subjects', error="some error occured"))

def admin_create_user_action(request, session):
    try:
        username = request.args.get('username', "")
        password = request.args.get('password', "")
        role = request.args.get('role', "")

        db.execute_query(f'''
            insert into `user`(username, password, role) values('{username}', '{password}', '{role}')
        ''')

        return redirect(url_for(f'admin_{role}s', success=f"{role} created successfully"))
    except Exception as e:
        print(e)
        return redirect(url_for(f'admin_{role}s', error="some error occured"))

def admin_edit_users_action(request, session):
    try:
        id = request.args.get('id', "")
        username = request.args.get('username', "")
        password = request.args.get('password', "")
        role = request.args.get('role', "")

        db.execute_query(f'''
            update `user`
            set username = '{username}',
            password = '{password}',
            role = '{role}'
            where id = {id}
        ''')

        return redirect(url_for(f'admin_{role}s', success=f"{role} edited successfully"))
    except Exception as e:
        print(e)
        return redirect(url_for(f'admin_{role}s', error="some error occured"))

def admin_delete_subject_action(request, session):
    try:
        subject = request.args.get('subject', "")
        db.execute_query(f'''
            delete from `subject` where id = {subject}
        ''')
        
        db.execute_query(f'''
            delete from `student_subject` where subject_id = {subject}
        ''')

        return redirect(url_for('admin_subjects', success="Subject deleted successfully"))
    except:
        return redirect(url_for('admin_subjects', error="some error occured"))