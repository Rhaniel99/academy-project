from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class BuildingController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM buildings")
            data = cur.fetchall()
            return render_template('public/buildingForm.html', username=session['username'], data=data)

    def post(self):
        msg = ''
        name = request.form['name_unity']
        adress = request.form['adress']
        rooms = request.form['rooms']

        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO buildings(name_unity, adress, rooms) VALUES (%s, %s, %s)",
                            (name, adress, rooms))
                cur.connection.commit()
                msg = 'Inserido com sucesso'
                return redirect(url_for('Building'))
            except:
                msg = 'Não foi inserido!'
        return render_template("public/buildingForm.html", msg=msg)


class DeleteBuildController(MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM buildings WHERE id = %s ", (id,))
            cur.connection.commit()
            return redirect(url_for('Building'))


class UpdateBuildController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM buildings WHERE id =%s ", (id,))
            one = cur.fetchone()
            return render_template('public/buildingupForm.html', one=one, username=session['username'])

    def post(self, id):
        msg = ''
        name = request.form['name_unity']
        adress = request.form['adress']
        rooms = request.form['rooms']

        with mysql.cursor() as cur:
            cur.execute("UPDATE buildings SET name_unity = %s, adress = %s, rooms = %s WHERE id = %s ", (name, adress, rooms, id))
            cur.connection.commit()
            return redirect(url_for('Building'))
