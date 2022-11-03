import bcrypt
from flask import Flask, render_template, request, redirect, flash, session, url_for
from src.database import mysql
from bcrypt import *


app = Flask(__name__)


@app.route("/index")
@app.route("/")
def homepage():
    return render_template("public/loginForm.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        with mysql.cursor() as cur:
            cur.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password))
            account = cur.fetchone()
            if len(account) > 0:
                if bcrypt.hashpw(password,  account[2].encode('utf-8')) == account[2].encode('utf-8'):
                    session['loggedin'] = True
                    session['id'] = account[0]
                    session['username'] = account[1]
                    return redirect(url_for('menu'))
            else:
                msg = 'Não é um adm, kekw'
    return render_template('public/loginForm.html', msg=msg)


@app.route("/menu")
def menu():
    return render_template('public/menuForm.html', username=session['username'])


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route("/teacher", methods=['GET'])
def teachers():
    if request.method == "GET":
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM teachers")
            data = cur.fetchall()
            return render_template('public/teacherForm.html', username=session['username'],  data=data)
    return redirect(url_for('login'))


@app.route("/regteacher", methods=['POST'])
def regteacher():
    if request.method == "POST":
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
                flash('Inserido com sucesso!', 'success')
            except:
                flash('Não foi inserido!', 'error')
            return redirect('/teacher')
    return render_template("public/teacherForm.html", username=session['username'])


@app.route("/deletetea/<int:reg_teacher>", methods=['POST'])
def deletetea(reg_teacher):
    if request.method == "POST":
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM teachers WHERE reg_teacher = %s ", (reg_teacher,))
            cur.connection.commit()
            return redirect('/teacher')


@app.route("/updatetea/<int:reg_teacher>", methods=['GET', 'POST'])
def updatetea(reg_teacher):
    if request.method == "GET":
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM teachers WHERE reg_teacher =%s ", (reg_teacher,))
            onetea = cur.fetchone()
            return render_template('public/teacherupForm.html', onetea=onetea,username=session['username'] )

    elif request.method == "POST":
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
                        "status_teacher = %s  WHERE reg_teacher = %s ",
                        (full_n_teacher, regtea, hist_vh_teacher, tittle_teacher, reg_w_teacher,
                         hiring_d_teacher,
                         close_d_teacher, status_teacher, reg_teacher))
            cur.connection.commit()
            return redirect('/teacher')


@app.route("/course", methods=['GET'])
def course():
    if request.method == "GET":
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM course")
            data = cur.fetchall()
        return render_template('public/courseForm.html', data=data)



@app.route("/regcourse", methods=['POST'])
def regcourse():
    if request.method == "POST":
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
                flash('Inserido com sucesso!', 'sucess')
            except:
                flash('Não foi inserido!', 'error')
            return redirect('/course')
    return render_template('public/courseForm.html')


@app.route("/classe", methods=['GET'])
def classe():
    if request.method == "GET":
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM class")
            data = cur.fetchall()
        return render_template('public/classForm.html', data=data)


@app.route("/regclasse", methods=['POST'])
def reglasse():
    if request.method == "POST":
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
            try:
                cur.execute(
                    "INSERT INTO class(institution, course,status_class, type_class, expected_numb_stud, "
                    "enrolled_numb_stud, semester, matrix_curriculum, turn_class, series_class ) VALUES (%s, %s, %s, "
                    "%s, %s, %s, %s, %s, %s, %s)",
                    (institution, course, status_class, type_class, expected_numb_stud, enrolled_numb_stud, semester,
                     matrix_curriculum, turn_class, series_class))
                cur.connection.commit()
                flash('Inserido com sucesso!', 'success')
            except:
                flash('Não foi inserido!', 'error')
            return redirect('/classe')
    return render_template("public/classForm.html")



@app.route("/discipline", methods=['GET', 'POST'])
def discipliners():
    if request.method == "GET":
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM discipline")
            data = cur.fetchall()
        return render_template('public/disciplineForm.html', data=data)

    if request.method == "POST":
        name_disclipline = request.form[' name_disclipline']
        discipline_workload_teory = request.form['discipline_workload_teory']
        discipline_workload_practice = request.form['discipline_workload_practice']
        discipline_workload_online = request.form['discipline_workload_online']
        discipline_workload_total = request.form[' discipline_workload_total']

        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO discipline( name_disclipline, discipline_workload_teory, "
                    "discipline_workload_practice,discipline_workload_online,discipline_workload_total ) VALUES (%s, "
                    "%s, %s, %s, %s, %s, %s, %s)",
                    (name_disclipline, discipline_workload_teory, discipline_workload_practice,
                     discipline_workload_online, discipline_workload_total))
                cur.connection.commit()
                flash('Inserido com sucesso!', 'success')
            except:
                flash('Não foi inserido!', 'error')
            return redirect('/discipline')
    return render_template("public/disciplineForm.html")
