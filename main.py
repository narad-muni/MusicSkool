from flask import Flask, session, request
from controllers import auth, templates_controller, admin, teacher_actions, teacher_views, student_actions, student_views
from utils import migrate

# Config

app = Flask(__name__)
app.secret_key = 'mein_nahi_bataunga'
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Templates

@app.route('/')
def index_template():
    return templates_controller.index_template(request, session)

@app.route('/login')
def login_template():
    return templates_controller.login_template(request, session)

@app.route('/admin_subjects')
def admin_subjects():
    return templates_controller.admin_subjects(request, session)

@app.route('/teacher_subjects')
def teacher_subjects():
    return teacher_views.teacher_subjects(request, session)

@app.route('/student_subjects')
def student_subjects():
    return student_views.student_subjects(request, session)

@app.route('/admin_students')
def admin_students():
    return templates_controller.admin_students(request, session)

@app.route('/admin_teachers')
def admin_teachers():
    return templates_controller.admin_teachers(request, session)

@app.route('/admin_attendance')
def admin_attendance():
    return templates_controller.admin_attendance(request, session)

@app.route('/admin_marks')
def admin_marks():
    return templates_controller.admin_marks(request, session)

@app.route('/teacher_attendance')
def teacher_attendance():
    return teacher_views.teacher_attendance(request, session)

@app.route('/teacher_marks')
def teacher_marks():
    return teacher_views.teacher_marks(request, session)


@app.route('/student_attendance')
def student_attendance():
    return student_views.student_attendance(request, session)

@app.route('/student_marks')
def student_marks():
    return student_views.student_marks(request, session)

@app.route('/admin_view_attendance')
def admin_view_attendance():
    return templates_controller.admin_view_attendance(request, session)
    
@app.route('/admin_create_subjects')
def admin_create_subjects():
    return templates_controller.admin_create_subjects(request, session)

@app.route('/admin_edit_subjects')
def admin_edit_subjects():
    return templates_controller.admin_edit_subjects(request, session)

@app.route('/admin_create_users')
def admin_create_users():
    return templates_controller.admin_create_users(request, session)

@app.route('/admin_edit_users')
def admin_edit_users():
    return templates_controller.admin_edit_users(request, session)

# Actions

@app.route('/login_action')
def login_action():
    return auth.login(request, session)

@app.route('/logout_action')
def logout_action():
    return auth.logout(request, session)

@app.route('/admin_create_subject_action')
def admin_create_subject_action():
    return admin.admin_create_subject_action(request, session)

@app.route('/admin_edit_subject_action')
def admin_edit_subject_action():
    return admin.admin_edit_subject_action(request, session)

@app.route('/admin_marks_action')
def admin_marks_action():
    return admin.admin_marks_action(request, session)

@app.route('/teacher_marks_action')
def teacher_marks_action():
    return teacher_actions.teacher_marks_action(request, session)

@app.route('/admin_delete_subject_action')
def admin_delete_subject_action():
    return admin.admin_delete_subject_action(request, session)

@app.route('/admin_create_user_action')
def admin_create_user_action():
    return admin.admin_create_user_action(request, session)

@app.route('/admin_edit_users_action')
def admin_edit_users_action():
    return admin.admin_edit_users_action(request, session)

@app.route('/admin_delete_users_action')
def admin_delete_users_action():
    return admin.admin_delete_users_action(request, session)

@app.route('/admin_add_student_subject_action')
def admin_add_student_subject_action():
    return admin.admin_add_student_subject_action(request, session)

@app.route('/admin_delete_student_subject_action')
def admin_delete_student_subject_action():
    return admin.admin_delete_student_subject_action(request, session)

@app.route('/admin_attendance_action')
def admin_attendance_action():
    return admin.admin_attendance_action(request, session)

@app.route('/teacher_attendance_action')
def teacher_attendance_action():
    return teacher_actions.teacher_attendance_action(request, session)

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

with app.app_context():
    try:
        migrate.init()
    except Exception as e:
        print("Server failed to start : ",e)


if __name__ == '__main__':
    app.run()
