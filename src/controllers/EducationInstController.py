from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class EducacationInstController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM education_institution")
            data = cur.fetchall()
        return render_template('public/educationForm.html', data=data, username=session['username'])

    def post(self):
        msg = ''
        corp = request.form['corporate_name']
        inst = request.form['institution_name']
        matrix = request.form['matrix']
        affiliated = request.form['affiliated']
        course = request.form['course']

        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO education_institution(corporate_name, institution_name, matrix, affiliated, "
                    "course) VALUES (%s, %s, "
                    "%s, %s, %s)",
                    (corp, inst, matrix, affiliated, course))
                cur.connection.commit()
                msg = 'Inserido com sucesso'
                return redirect(url_for('EducationInstitution'))
            except:
                msg = 'Não foi inserido!'
        return render_template("public/educationForm.html", msg=msg)


class DeleteEduInstController(MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM education_institution WHERE id = %s ", (id,))
            cur.connection.commit()
            return redirect(url_for('EducationInstitution'))


class UpdateEduInstController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM education_institution WHERE id =%s ", (id,))
            one = cur.fetchone()
            return render_template('public/educationupForm.html', one=one, username=session['username'])

    def post(self, id):
        msg = ''
        corp = request.form['corporate_name']
        inst = request.form['institution_name']
        matrix = request.form['matrix']
        affiliated = request.form['affiliated']
        course = request.form['course']

        with mysql.cursor() as cur:
            cur.execute("UPDATE education_institution SET corporate_name = %s, institution_name = %s, matrix = %s, "
                        "affiliated = %s, course = %s WHERE id = %s ", (corp, inst, matrix, affiliated, course, id))
            cur.connection.commit()
            return redirect(url_for('EducationInstitution'))



