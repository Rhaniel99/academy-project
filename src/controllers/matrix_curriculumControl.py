from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class InsertControlMatrixCurriculum(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM matrix_curriculum")
            data = cur.fetchall()
         return render_template('public/courseForm.html', data = data)


    def post(self): 
        date_start = request.form['date_start']
        course = request.form['course']
       
        

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO matrix_curriculum(date_start, course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (date_start, course))
            cur.connection.commit()
            return redirect('/') 