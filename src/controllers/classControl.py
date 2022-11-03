from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class InsertControlClass(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM class")
            data = cur.fetchall()
         return render_template('public/courseForm.html', data = data)


    def post(self): 
        institution = request.form['institution']
        course = request.form['course']
        status_class = request.form['status_class']
        type_class = request.form['type_class']
        expected_numb_stud = request.form['expected_numb_stud']
        enrolled_numb_stud = request.form['enrolled_numb_stud']
        semester = request.form['semester']
        matrix_curriculum = request.form['matrix_curriculum']
        turn_class = request.form['turn_class']
        series_class = request.form['series_class']

        

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO class(institution, course,status_class, type_class, expected_numb_stud, enrolled_numb_stud, semester, matrix_curriculum, turn_class, series_class ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (institution, course, status_class,type_class, expected_numb_stud, enrolled_numb_stud, semester,matrix_curriculum, turn_class, series_class))
            cur.connection.commit()
            return redirect('/')