from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class Academic_PeriodController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM academic_period")
            data = cur.fetchall()
            return render_template('public/academic_periodForm.html', username=session['username'], data=data)

    def post(self):
        msg = ''
        academic_period_name = request.form['academic_period_name']
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        academic_period_description = request.form['academic_period_description']

        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO academic_period(academic_period_name, date_start, date_end, "
                            "academic_period_description ) VALUES (%s, %s, %s, %s)",
                            (academic_period_name, date_start, date_end, academic_period_description))
                cur.connection.commit()
                msg = 'Inserido com sucesso'
                return redirect(url_for('Academic_Period'))
            except:
                msg = 'Não foi inserido!'
        return render_template("public/academic_periodForm.html", msg=msg)


class DeleteAcademic_PeriodController(MethodView):
    def post(self, id_period):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM academic_period WHERE id_period = %s ", (id_period,))
            cur.connection.commit()
            return redirect(url_for('Academic_Period'))


class UpdateAcademic_PeriodController(MethodView):
    def get(self, id_period):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM academic_period WHERE id_period =%s ", (id_period,))
            one = cur.fetchone()
            return render_template('public/academic_periodupForm.html', one=one, username=session['username'])

    def post(self, id_period):
        academic_period_name = request.form['academic_period_name']
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        academic_period_description = request.form['academic_period_description']

        with mysql.cursor() as cur:
            cur.execute("UPDATE academic_period SET academic_period_name = %s, date_start = %s, date_end = %s, "
                        "academic_period_description = %s WHERE id_period = %s ",
                        (academic_period_name, date_start, date_end, academic_period_description, id_period))
            cur.connection.commit()
            return redirect(url_for('Academic_Period'))
