from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class ClassController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM class")
            data = cur.fetchall()
            return render_template('public/classForm.html', username=session['username'], data=data)

    def post(self):
            msg = ''
            institution = request.form['institution']
            course = request.form['course_name']
            status_class = request.form['status_class']
            type_class = request.form['type_class']
            expected_numb_stud = request.form['expected_numb_stud']
            enrolled_numb_stud = request.form['enrolled_numb_stud']
            semester = request.form['semester']
            code_class = request.form['code_class']
            matrix_curriculum = request.form['matrix_curriculum']
            turn_class = request.form['turn_class']
            series_class = request.form['series_class']

            with mysql.cursor() as cur:
                try:
                    cur.execute("INSERT INTO class(institution, course_name,code_class, status_class, type_class, "
                                "expected_numb_stud, "
                                "enrolled_numb_stud, semester, matrix_curriculum, turn_class, series_class ) VALUES ("
                                "%s, %s, %s, "
                                "%s, %s, %s, %s, %s, %s, %s, %s)",
                                (institution, course,code_class, status_class, type_class, expected_numb_stud, enrolled_numb_stud,
                                 semester,
                                 matrix_curriculum, turn_class, series_class))
                    cur.connection.commit()
                    msg = 'Inserido com sucesso'
                    return redirect(url_for('Class'))
                except:
                    msg = 'Não foi inserido!'
            return render_template("public/classForm.html", msg=msg)


class DeleteClassController(MethodView):
     def post(self, id_class):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM class WHERE id_class = %s ", (id_class,))
            cur.connection.commit()
            return redirect(url_for('Class'))


class UpdateClassController(MethodView):
    def get(self, id_class):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM class WHERE id_class =%s ", (id_class,))
            onetea = cur.fetchone()
            return render_template('public/classupForm.html', onetea=onetea, username=session['username'])

    def post(self, id_class):
        institution = request.form['institution']
        course = request.form['course']
        status_class = request.form['status_class']
        type_class = request.form['type_class']
        expected_numb_stud = request.form['expected_numb_stud']
        enrolled_numb_stud = request.form['enrolled_numb_stud']
        semester = request.form['semester']
        matrix_curriculum = request.form['matrix_curriculum']
        turn_class = request.form['turn_class']
        series_class = request.form['series_class']

        with mysql.cursor() as cur:
            cur.execute("UPDATE class SET institution = %s, course_name = %s, status_class = %s, type_class = %s, "
                        "expected_numb_stud = %s, enrolled_numb_stud = %s, semester = %s, matrix_curriculum = %s, "
                        "turn_class = %s, series_class = %s  WHERE id_class = %s ",
                        (institution, course, status_class, type_class, expected_numb_stud, enrolled_numb_stud,
                         semester,
                         matrix_curriculum, turn_class, series_class, id_class))
            cur.connection.commit()
            return redirect(url_for('Class'))



