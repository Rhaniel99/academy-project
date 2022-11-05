from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class TeacherController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM teachers")
            data = cur.fetchall()

            cur.execute("SELECT status_teacher FROM teachers")
            status = cur.fetchall()

            return render_template('public/teacherForm.html', username=session['username'], data=data, status=status)

    def post(self):
        msg = ''
        full_n_teacher = request.form['full_n_teacher']
        register_teacher = request.form['register_teacher']
        hist_vh_teacher = request.form['hist_vh_teacher']
        tittle_teacher = request.form['tittle_teacher']
        reg_w_teacher = request.form['reg_w_teacher']
        hiring_d_teacher = request.form['hiring_d_teacher']
        close_d_teacher = request.form['close_d_teacher']
        status_teacher = request.form['status_teacher']

        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO teachers(full_n_teacher, reg_teacher, hist_vh_teacher, tittle_teacher, "
                            "regime_w_teacher, d_hiring_teacher, d_close_teacher, status_teacher) VALUES (%s, %s, %s, "
                            "%s, "
                            "%s, %s, %s, %s)",
                            (full_n_teacher, register_teacher, hist_vh_teacher, tittle_teacher, reg_w_teacher,
                             hiring_d_teacher,
                             close_d_teacher, status_teacher))
                cur.connection.commit()
                msg = 'Inserido com sucesso'
                return redirect(url_for('Teacher'))
            except:
                msg = 'Não foi inserido!'
        return render_template("public/teacherForm.html", msg=msg)


class DeleteTeacherController(MethodView):
    def post(self, id_teacher):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM teachers WHERE id_teacher = %s ", (id_teacher,))
            cur.connection.commit()
            return redirect(url_for('Teacher'))


class UpdateTeacherController(MethodView):
    def get(self, id_teacher):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM teachers WHERE id_teacher =%s ", (id_teacher,))
            onetea = cur.fetchone()
            return render_template('public/teacherupForm.html', onetea=onetea, username=session['username'])

    def post(self, id_teacher):
        full_n_teacher = request.form['full_n_teacher']
        regtea = request.form['register_teacher']
        hist_vh_teacher = request.form['hist_vh_teacher']
        tittle_teacher = request.form['tittle_teacher']
        reg_w_teacher = request.form['reg_w_teacher']
        hiring_d_teacher = request.form['hiring_d_teacher']
        close_d_teacher = request.form['close_d_teacher']
        status_teacher = request.form['status_teacher']

        with mysql.cursor() as cur:
            cur.execute("UPDATE teachers SET full_n_teacher = %s, reg_teacher = %s, hist_vh_teacher = %s, "
                        "tittle_teacher = %s, regime_w_teacher = %s, d_hiring_teacher = %s, d_close_teacher = %s, "
                        "status_teacher = %s  WHERE id_teacher = %s ",
                        (full_n_teacher, regtea, hist_vh_teacher, tittle_teacher, reg_w_teacher,
                         hiring_d_teacher,
                         close_d_teacher, status_teacher, id_teacher))
            cur.connection.commit()
            return redirect(url_for('Teacher'))

