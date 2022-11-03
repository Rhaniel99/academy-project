from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class InsertControlCourse(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM course")
            data = cur.fetchall()
         return render_template('public/courseForm.html', data = data)


    def post(self): 
        full_n_course = request.form['full_n_course']
        short_n_course = request.form['short_n_course']
        modal_course = request.form['modal_course']
        class_course = request.form['class_course']
        

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO course(full_n_course, short_n_course, modal_course, class_course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (full_n_course, short_n_course, modal_course, class_course))
            cur.connection.commit()
            return redirect('/') 