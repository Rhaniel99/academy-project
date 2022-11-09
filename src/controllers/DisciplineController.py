from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class DisciplineController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM discipline")
            data = cur.fetchall()
            return render_template('public/disciplineForm.html', username=session['username'], data=data)

    def post(self):
        msg = ''
        name_discipline = request.form['name_discipline']
        discipline_workload_teory = request.form['discipline_workload_teory']
        discipline_workload_practice = request.form['discipline_workload_practice']
        discipline_workload_online = request.form['discipline_workload_online']
        discipline_workload_total = request.form['discipline_workload_total']

        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO discipline( name_discipline, discipline_workload_teory, "
                    "discipline_workload_practice,discipline_workload_online,discipline_workload_total ) VALUES (%s, "
                    "%s, %s, %s, %s)",
                    (name_discipline, discipline_workload_teory, discipline_workload_practice,
                     discipline_workload_online, discipline_workload_total))
                cur.connection.commit()
                msg = 'Inserido com sucesso'
                return redirect(url_for('Discipline'))
            except:
                msg = 'Não foi inserido!'
        return render_template("public/disciplineForm.html", msg=msg)


class DeleteDisciplineController(MethodView):
    def post(self, id_discipline):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM discipline WHERE id_discipline = %s ", (id_discipline,))
            cur.connection.commit()
            return redirect(url_for('Discipline'))


class UpdateDisciplineController(MethodView):
    def get(self, id_discipline):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM discipline WHERE id_discipline =%s ", (id_discipline,))
            onetea = cur.fetchone()
            return render_template('public/disciplineupForm.html', onetea=onetea, username=session['username'])

    def post(self, id_discipline):
        name_discipline = request.form['name_discipline']
        discipline_workload_teory = request.form['discipline_workload_teory']
        discipline_workload_practice = request.form['discipline_workload_practice']
        discipline_workload_online = request.form['discipline_workload_online']
        discipline_workload_total = request.form[' discipline_workload_total']

        with mysql.cursor() as cur:
            cur.execute("UPDATE discipline SET name_discipline = %s, discipline_workload_teory = %s, "
                        "discipline_workload_practice = %s, discipline_workload_online = %s, "
                        "discipline_workload_total = %s  WHERE id_discipline = %s ",
                        (name_discipline, discipline_workload_teory, discipline_workload_practice,
                         discipline_workload_online, discipline_workload_total, id_discipline))
            cur.connection.commit()
            return redirect(url_for('Discipline'))
