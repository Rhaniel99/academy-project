from flask import render_template, request, redirect, session, url_for
from src.database import mysql
from flask.views import MethodView


class IndexController(MethodView):
    def get(self):
        return render_template('public/loginForm.html')

    def post(self):
        msg = ''
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        with mysql.cursor() as cur:
            cur.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password))
            account = cur.fetchone()
            if len(account) > 0:
                session['loggedin'] = True
                session['id'] = account[0]
                session['username'] = account[1]
                return redirect(url_for('Menu'))
            else:
                msg = 'Não é um adm, kekw'
            return render_template('public/loginForm.html', msg=msg)

