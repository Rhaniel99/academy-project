from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class CourseController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM course")
            data = cur.fetchall()
        return render_template('public/courseForm.html', data=data, username=session['username'])

    def post(self):
        msg = ''
        full_n_course = request.form['full_n_course']
        short_n_course = request.form['short_n_course']
        modal_course = request.form['modal_course']
        class_course = request.form['class_course']

        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO course(full_n_course, short_n_course, modal_course, class_course) VALUES (%s, %s, "
                    "%s, %s)",
                    (full_n_course, short_n_course, modal_course, class_course))
                cur.connection.commit()
                msg = 'Inserido com sucesso'
                return redirect(url_for('Course'))
            except:
                msg = 'Não foi inserido!'
        return render_template("public/courseForm.html", msg=msg)


class DeleteCourseController(MethodView):
    def post(self, id_course):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM course WHERE id_course = %s ", (id_course,))
            cur.connection.commit()
            return redirect(url_for('Course'))


class UpdateCourseController(MethodView):
    def get(self, id_course):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM course WHERE id_course =%s ", (id_course,))
            one = cur.fetchone()
            return render_template('public/courseupForm.html', one=one, username=session['username'])

    def post(self, id_course):
        msg = ''
        full_n_course = request.form['full_n_course']
        short_n_course = request.form['short_n_course']
        modal_course = request.form['modal_course']
        class_course = request.form['class_course']

        with mysql.cursor() as cur:
            cur.execute("UPDATE course SET full_n_course = %s, short_n_course = %s, modal_course = %s, "
                        "class_course = %s WHERE id_course = %s ", (full_n_course, short_n_course, modal_course, class_course, id_course))
            cur.connection.commit()
            return redirect(url_for('Course'))




