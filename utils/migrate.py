from utils.db import execute_query, reload_cnx, old_cnx

def poppulate():
    old_cnx()

    execute_query("DROP DATABASE IF EXISTS MusicSchool;")

    execute_query("CREATE DATABASE MusicSchool;")

    reload_cnx()

    generate_schema()

    poppulate_data()

def init():
    old_cnx()

    db_exists = execute_query("SHOW DATABASES LIKE 'MusicSchool';")

    if(not db_exists):
        execute_query("CREATE DATABASE MusicSchool;")

        reload_cnx()

        generate_schema()
        poppulate_data()
        
    else:
        reload_cnx()


def generate_schema():

    #User
    execute_query('''
        CREATE TABLE IF NOT EXISTS `user` (
            `id` INT AUTO_INCREMENT PRIMARY KEY,
            `username` VARCHAR(255),
            `password` VARCHAR(255),
            `role` VARCHAR(50)
        );
    ''')

    #Subject
    execute_query('''
        CREATE TABLE IF NOT EXISTS `subject` (
            `id` INT AUTO_INCREMENT PRIMARY KEY,
            `name` VARCHAR(255),
            `instrument` VARCHAR(255),
            `teacher_id` INT
        );
    ''')

    #Attendence
    execute_query('''
        CREATE TABLE IF NOT EXISTS `attendence` (
            `id` INT AUTO_INCREMENT PRIMARY KEY,
            `user_id` INT,
            `subject_id` INT,
            `status` VARCHAR(10),
            `date` DATE DEFAULT CURRENT_DATE
        );
    ''')

    #Marks
    execute_query('''
        CREATE TABLE IF NOT EXISTS `marks` (
            `id` INT AUTO_INCREMENT PRIMARY KEY,
            `subject_id` INT,
            `user_id` INT,
            `marks` INT
        );
    ''')

    #Student Subject
    execute_query('''
        CREATE TABLE IF NOT EXISTS `student_subject` (
            `id` INT AUTO_INCREMENT PRIMARY KEY,
            `subject_id` INT,
            `user_id` INT
        );
    ''')

def poppulate_data():
    execute_query('''
        INSERT INTO `user`(
            username, password, role
        )
        values(
            'admin',
            'admin123',
            'admin'
        ),
        (
            'student',
            'student123',
            'student'
        ),
        (
            'teacher',
            'teacher123',
            'teacher'
        ),
        (
            'student2',
            'student123',
            'student'
        ),
        (
            'teacher2',
            'teacher123',
            'teacher'
        )
    ''')

    execute_query('''
        INSERT INTO `subject`(
            name, instrument, teacher_id
        )
        values(
            'Beat Boxer',
            'Hands & Mouth',
            '3'
        ),
        (
            'Indian Classical',
            'Tabla',
            '5'
        ),
        (
            'Rockstar',
            'Drum Set',
            '3'
        )
    ''')

    execute_query('''
        INSERT into `student_subject`(subject_id, user_id)
        values(1,2)
    ''')