from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class TeacherController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM teachers")
            data = cur.fetchall()
            return render_template('public/teacherForm.html', username=session['username'], data=data)

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


