from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class PlanningController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM plannings")
            data = cur.fetchall()
            return render_template('public/planningForm.html', username=session['username'], data=data)

    def post(self):
        msg = ''
        semester = request.form['semester']
        class1 = request.form['class1']
        discipline = request.form['discipline']
        teacher = request.form['teacher']
        workload = request.form['workload']
        modalit_offering = request.form['modalit_offering']
        status = request.form['status']

        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO plannings(semester, class, discipline, teacher, "
                            "workload, modalit_offering, status ) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (semester, class1, discipline, teacher, workload, modalit_offering, status))
                cur.connection.commit()
                msg = 'Inserido com sucesso'
                return redirect(url_for('Planning'))
            except:
                msg = 'Não foi inserido!'
        return render_template("public/planningForm.html", msg=msg)


class DeletePlanController(MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM plannings WHERE id = %s ", (id,))
            cur.connection.commit()
            return redirect(url_for('Planning'))


class UpdatePlanController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM plannings WHERE id =%s ", (id,))
            one = cur.fetchone()
            return render_template('public/planningupForm.html', one=one, username=session['username'])

    def post(self, id):
        msg = ''
        semester = request.form['semester']
        class1 = request.form['class1']
        discipline = request.form['discipline']
        teacher = request.form['teacher']
        workload = request.form['workload']
        modalit_offering = request.form['modalit_offering']
        status = request.form['status']

        with mysql.cursor() as cur:
            cur.execute("UPDATE plannings SET semester = %s, class = %s, discipline = %s, "
                        "teacher = %s, workload = %s, modalit_offering = %s, status = %s "
                        "WHERE id = %s ",
                        (semester, class1, discipline, teacher, workload,
                         modalit_offering, status, id))
            cur.connection.commit()
            return redirect(url_for('Planning'))
