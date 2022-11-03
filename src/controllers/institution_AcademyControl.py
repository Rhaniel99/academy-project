from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class InsertControlInstitutionAcademy(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM institution_academy")
            data = cur.fetchall()
         return render_template('public/courseForm.html', data = data)


    def post(self): 
        
        institution_name = request.form['institution_name']
        headquarters = request.form['headquarters']
        branch = request.form['branch']
        courses  = request.form[' courses ']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO institution_academy(institution_name, headquarters, branch, courses) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (institution_name, headquarters, branch, courses))
            cur.connection.commit()
            return redirect('/') 