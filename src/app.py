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
app.add_url_rule(routes["insert_route_discipline"], view_func=routes["insert_controller_discipline"])
app.add_url_rule(routes["delete_route_discipline"], view_func=routes["delete_controller_discipline"])
app.add_url_rule(routes["update_route_discipline"], view_func=routes["update_controller_discipline"])
app.add_url_rule(routes["insert_route_plan"], view_func=routes["insert_controller_plan"])
app.add_url_rule(routes["delete_route_plan"], view_func=routes["delete_controller_plan"])
app.add_url_rule(routes["update_route_plan"], view_func=routes["update_controller_plan"])
app.add_url_rule(routes["insert_route_building"], view_func=routes["insert_controller_building"])
app.add_url_rule(routes["delete_route_building"], view_func=routes["delete_controller_building"])
app.add_url_rule(routes["update_route_building"], view_func=routes["update_controller_building"])
app.add_url_rule(routes["insert_route_education"], view_func=routes["insert_controller_education"])
app.add_url_rule(routes["delete_route_education"], view_func=routes["delete_controller_education"])
app.add_url_rule(routes["update_route_education"], view_func=routes["update_controller_education"])


