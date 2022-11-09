from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class Matrix_CurriculumController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM matrix_curriculum")
            data = cur.fetchall()
            return render_template('public/matrix_curriculumForm.html', username=session['username'], data=data)

    def post(self):
        msg = ''
        date_start = request.form['date_start']
        cod = request.form['cod']
        course = request.form['course']
        discipline = request.form['discipline']
        period = request.form['period']

        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO matrix_curriculum(date_start, cod, course, discipline, period ) VALUES (%s, "
                            "%s, %s, %s, %s )",
                            (date_start, cod, course, discipline, period))
                cur.connection.commit()
                msg = 'Inserido com sucesso'
                return redirect(url_for('Matrix_Curriculum'))
            except:
                msg = 'Não foi inserido!'
        return render_template("public/matrix_curriculumForm.html", msg=msg)


class DeleteMatrix_CurriculumController(MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM matrix_curriculum WHERE id = %s ", (id,))
            cur.connection.commit()
            return redirect(url_for('Matrix_Curriculum'))



class UpdateMatrix_CurriculumController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM matrix_curriculum WHERE id =%s ", (id,))
            one = cur.fetchone()
            return render_template('public/matrix_curriculumupForm.html', one=one, username=session['username'])

    def post(self, id):
        date_start = request.form['date_start']
        cod = request.form['cod']
        course = request.form['course']
        discipline = request.form['discipline']
        period = request.form['period']

        with mysql.cursor() as cur:
            cur.execute("UPDATE matrix_curriculum SET date_start = %s, cod = %s, course = %s, discipline = %s, "
                        "period = %s WHERE id = %s ",
                        (date_start, cod, course, discipline, period, id))
            cur.connection.commit()
            return redirect(url_for('Matrix_Curriculum'))


