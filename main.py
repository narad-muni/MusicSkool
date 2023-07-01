from flask import Flask, session, request
from controllers import auth, templates_controller, admin
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

@app.route('/admin_students')
def admin_students():
    return templates_controller.admin_students(request, session)

@app.route('/admin_teachers')
def admin_teachers():
    return templates_controller.admin_teachers(request, session)

@app.route('/admin_attendance')
def admin_attendance():
    return templates_controller.admin_attendance(request, session)

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
        migrate.poppulate()
        # migrate.init()
    except Exception as e:
        print("Server failed to start : ",e)


if __name__ == '__main__':
    app.run()
