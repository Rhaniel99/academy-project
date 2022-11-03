from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class InsertControlBuilding(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM building")
            data = cur.fetchall()
         return render_template('public/courseForm.html', data = data)


    def post(self): 
        adress = request.form['adress']
      
        

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO building(adress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  (adress))
            cur.connection.commit()
            return redirect('/') 