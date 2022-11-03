from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class InsertControlDiscipline(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM discipline")
            data = cur.fetchall()
         return render_template('public/courseForm.html', data = data)


    def post(self): 
        name_disclipline = request.form[' name_disclipline']
        discipline_workload_teory = request.form['discipline_workload_teory']
        discipline_workload_practice = request.form['discipline_workload_practice']
        discipline_workload_online = request.form['discipline_workload_online']
        discipline_workload_total = request.form[' discipline_workload_total']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO discipline( name_disclipline, discipline_workload_teory, discipline_workload_practice,discipline_workload_online,discipline_workload_total ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (name_disclipline, discipline_workload_teory, discipline_workload_practice, discipline_workload_online, discipline_workload_total))
            cur.connection.commit()
            return redirect('/') 