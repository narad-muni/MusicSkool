from utils.db import execute_query, make_db
import os

def poppulate():
    if(os.path.exists("music_school.db")):
        os.remove("music_school.db")

    make_db()

    generate_schema()

    poppulate_data()

def init():

    if(not os.path.exists("music_school.db")):

        make_db()

        generate_schema()

        poppulate_data()

    else:
        make_db()


def generate_schema():

    #User
    execute_query('''
        CREATE TABLE IF NOT EXISTS `user` (
            `id` INTEGER  PRIMARY KEY AUTOINCREMENT,
            `username` VARCHAR(255),
            `password` VARCHAR(255),
            `role` VARCHAR(50)
        );
    ''')

    #Subject
    execute_query('''
        CREATE TABLE IF NOT EXISTS `subject` (
            `id` INTEGER  PRIMARY KEY AUTOINCREMENT,
            `name` VARCHAR(255),
            `instrument` VARCHAR(255),
            `teacher_id` INT
        );
    ''')

    #Attendence
    execute_query('''
        CREATE TABLE IF NOT EXISTS `attendance` (
            `id` INTEGER  PRIMARY KEY AUTOINCREMENT,
            `student_id` INT,
            `subject_id` INT,
            `status` VARCHAR(50),
            `date` DATE DEFAULT CURRENT_DATE
        );
    ''')

    #Marks
    execute_query('''
        CREATE TABLE IF NOT EXISTS `marks` (
            `id` INTEGER  PRIMARY KEY AUTOINCREMENT,
            `subject_id` INT,
            `student_id` INT,
            `marks` INT
        );
    ''')

    #Student Subject
    execute_query('''
        CREATE TABLE IF NOT EXISTS `student_subject` (
            `id` INTEGER  PRIMARY KEY AUTOINCREMENT,
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