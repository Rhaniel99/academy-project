from flask import render_template, session
from flask.views import MethodView


class MenuController(MethodView):
    def get(self):
        return render_template('public/menuForm.html', username=session['username'])

