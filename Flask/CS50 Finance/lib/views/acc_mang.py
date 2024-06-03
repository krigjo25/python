#   Importing responsories
import time

from markupsafe import Markup
from flask.views import MethodView
from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, redirect, url_for, request, session, flash

#   Importing cs50 libraries
from cs50 import SQL
from lib.cs50.helpers import apology, login_required

class ManageAccounts(MethodView):

    #   Class variables
    methods = ['GET', 'POST']
    __db__ = SQL('sqlite:///finance.db')


    def get(self):
        if request.path == '/register': return render_template('register.html')
        elif request.path == '/login': return render_template('login.html')
        elif request.path == '/settings': return render_template('settings.html')
        elif request.path == '/logout': return self.logout()

        return

    def post(self):

        #   Register a user
        if request.method == 'POST' and request.path =='/register': return self.CreateUser()

        #   log the user in
        elif request.method == 'POST' and request.path =='/login': return self.login()
        elif request.method == 'POST' and request.path =='/settings': return self.Settings()



    def CreateUser(self):

        try: #  Examine for Exceptions

                #   Ensure the user has inputted the fields
                if not request.form['username'] or not request.form['password'] or not request.form['confirmation']: raise Exception('User name / password left blank')

                #   Ensure the user name is unique
                for key in self.__db__.execute("SELECT * FROM users;"):
                    if key['username'] == request.form['username']: raise Exception('Username unavailable')

                #   Ensure the passwords matches
                if request.form['password'] != request.form['confirmation']: raise Exception('passwords miss match')

        except Exception as e: return apology(f"{e}", 400)

        #   Insert a new Record
        self.__db__.execute('INSERT INTO users (username, hash) VALUES (?,?)', request.form['username'], generate_password_hash(request.form['confirmation']) )

        flash("Registration Complete, Thank you for registering on this site.")
        return render_template('login.html')

    def login(self):
        """Log user in"""

        # Forget any user_id
        session.clear()
         #   Fetch user data
        records = self.__db__.execute( "SELECT * FROM users WHERE username = ?", request.form['username'])


        try:

            # Ensure username and password was submitted
            if not request.form['username'] or not request.form['password']: raise Exception('Username and/or password is left blank')

            #   Ensure the password is correct
            if len(records) != 1 or not check_password_hash(records[0]["hash"], request.form['password']):
                raise Exception('Username or password is Invalid')

        except Exception as e: return apology(f"{e}", 403)

        #   Send a message to the user
        flash(Markup(f'Welcome back <b>{records[0]['username']}</b> !'), 'Success')

        # Remember which user has logged in
        session["user_id"] = records[0]['id']

        #   Clear memory
        del records

        return redirect('/')

    def logout(self):

        # Forget any user_id
        session.clear()

        # Redirect user to login form
        flash("Good bye, enjoy your day !")
        return redirect(url_for('login.html'))

    @login_required
    def Settings(self):

        #   Initialize databases
        user = self.__db__.execute('SELECT * FROM users WHERE id = ?;', session['user_id'])

        try:

            if len(user) != 1 or not check_password_hash(user[0]["hash"], request.form['confirmation']): raise Exception('Old password missmatch')

            #   Change username
            if request.form['username']:
                try:
                    #   Ensure the user name is unique
                    for key in self.__db__.execute("SELECT * FROM users WHERE id = ?;", session['user_id']):
                        if key['username'] == request.form['username']: raise Exception('Username unavailable')
                except Exception as e: return apology(f"{e}", 400)

                #   Update the username
                self.__db__.execute('UPDATE users SET username = ? WHERE id = ?;', request.form['username'], session['user_id'])
                #   Rename table
                self.__db__.execute('ALTER TABLE ? RENAME TO ?;', user[0]['username'], request.form['username'])

                flash('Username Changes Saved')



            #   Change password
            if request.form['password']:
                try:
                    #   Ensure the passwords matches
                    if request.form['password'] != request.form['match_pass']: raise Exception('passwords miss match')
                    if not check_password_hash(user[0]["hash"], request.form['confirmation']): raise Exception('Old password miss match')

                except Exception as e: return apology(f"{e}", 400)
                self.__db__.execute('UPDATE users SET hash = ? WHERE id = ?;', generate_password_hash(request.form['match_pass']), session['user_id'])
                flash('Password Changes Saved')

            return render_template('index.html', userinfo= self.__db__.execute('SELECT username, cash, total, stock_value FROM users WHERE id = ?;', session['user_id']),  stocks= self.__db__.execute('SELECT  abbrivation, qty, price, total FROM ?;',  user[0]['username']), history=self.__db__.execute('SELECT * FROM trading_history WHERE user_id = ?;', int(session['user_id'])))


        except Exception as e: return apology(f"{e}", 400)



