from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class InsertControlAcademicPeriod(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM academic_period")
            data = cur.fetchall()
         return render_template('public/courseForm.html', data = data)


    def post(self): 
        academic_period_name = request.form[' academic_period_name']
        date_start = request.form['date_start']
        date_end = request.form[' date_end']
        academic_period_description = request.form['academic_period_description']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO academic_period(academic_period_name, date_start, date_end, academic_period_description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (academic_period_name, date_start, date_end, academic_period_description))
            cur.connection.commit()
            return redirect('/') 