from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class InsertControlPlanning(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM planning")
            data = cur.fetchall()
         return render_template('public/courseForm.html', data = data)


    def post(self): 
        semester = request.form['semester']
        planning_class = request.form[' planning_class']
        planning_status = request.form['planning_status']
        planning_workload = request.form['planning_workload']
        modalit_offering = request.form['modalit_offering']
        planning_subject = request.form['planning_subject']
        

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO planning(full_n_course, short_n_course, modal_course, class_course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (semester,planning_class,planning_status,planning_workload,modalit_offering,planning_subject))
            cur.connection.commit()
            return redirect('/') 