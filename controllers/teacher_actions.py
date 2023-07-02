from flask import jsonify, redirect, url_for
from utils import db
import traceback

def teacher_marks_action(request, session):
    try:
        student_id = request.args.get('student_id', "")
        subject_id = request.args.get('subject_id', "")
        marks = request.args.get('marks', "")

        db.execute_query(f'''
            update `marks`
            set marks = {marks}
            where student_id = {student_id}
            and subject_id = {subject_id}
        ''')

        return redirect(url_for(f'teacher_marks', success="Marks updated successfully"))
    except:
        print(traceback.print_exc())
        return redirect(url_for(f'teacher_marks', error="some error occured"))

def teacher_attendance_action(request, session):
    try:
        status = request.args.get("status")
        student_id = request.args.get("student_id")
        subject_id = request.args.get("subject_id")

        data = db.execute_query(f'''
            delete from `attendance`
            where subject_id = {subject_id}
            and student_id = {student_id}
            and `date` = CURDATE()
        ''')

        data = db.execute_query(f'''
            insert into `attendance`(subject_id, status, student_id, `date`)
            values(
                '{subject_id}',
                '{status}',
                '{student_id}',
                CURDATE()
            )
        ''')

        return redirect(url_for(f'teacher_attendance', success=f"attendance marked successfully"))
    except Exception as e:
        print(traceback.print_exc())
        return redirect(url_for('teacher_attendance', error="some error occured"))