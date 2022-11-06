from flask import Flask, render_template, request, redirect, flash, session, url_for
from src.database import mysql
from src.routes.routes import *
app = Flask(__name__)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('Index'))


app.add_url_rule(routes["index_route"], view_func=routes["indexcontroller"])
app.add_url_rule(routes["menu_route"], view_func=routes["menucontroller"])
app.add_url_rule(routes["insert_route_teacher"], view_func=routes["insert_controller_teacher"])
app.add_url_rule(routes["delete_route_teacher"], view_func=routes["delete_controller_teacher"])
app.add_url_rule(routes["update_route_teacher"], view_func=routes["update_controller_teacher"])
app.add_url_rule(routes["insert_route_course"], view_func=routes["insert_controller_course"])
app.add_url_rule(routes["delete_route_course"], view_func=routes["delete_controller_course"])
app.add_url_rule(routes["update_route_course"], view_func=routes["update_controller_course"])
app.add_url_rule(routes["insert_route_class"], view_func=routes["insert_controller_class"])
app.add_url_rule(routes["delete_route_class"], view_func=routes["delete_controller_class"])
app.add_url_rule(routes["update_route_class"], view_func=routes["update_controller_class"])
app.add_url_rule(routes["insert_route_plan"], view_func=routes["insert_controller_plan"])
app.add_url_rule(routes["delete_route_plan"], view_func=routes["delete_controller_plan"])
app.add_url_rule(routes["update_route_plan"], view_func=routes["update_controller_plan"])


# Discipline
@app.route("/discipline", methods=['GET'])
def discipliners():
    if request.method == "GET":
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM discipline")
            data = cur.fetchall()
        return render_template('public/disciplineForm.html', data=data, username=session['username'])


@app.route("/regdiscipline", methods=['POST'])
def regdiscipline():
    if request.method == "POST":
        name_discipline = request.form['name_discipline']
        discipline_workload_teory = request.form['discipline_workload_teory']
        discipline_workload_practice = request.form['discipline_workload_practice']
        discipline_workload_online = request.form['discipline_workload_online']
        discipline_workload_total = request.form[' discipline_workload_total']
        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO discipline( name_discipline, discipline_workload_teory, "
                    "discipline_workload_practice,discipline_workload_online,discipline_workload_total ) VALUES (%s, "
                    "%s, %s, %s, %s)",
                    (name_discipline, discipline_workload_teory, discipline_workload_practice,
                     discipline_workload_online, discipline_workload_total))
                cur.connection.commit()
                flash('Inserido com sucesso!', 'success')
            except:
                flash('Não foi inserido!', 'error')
            return redirect('/discipline')
    return render_template("public/disciplineForm.html")


@app.route("/deletedisci/<int:id_discipline>", methods=['POST'])
def deletedisci(id_discipline):
    if request.method == "POST":
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM discipline WHERE id_discipline = %s ", (id_discipline,))
            cur.connection.commit()
            return redirect('/discipline')
