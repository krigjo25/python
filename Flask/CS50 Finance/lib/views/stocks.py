#   Import responsories
from markupsafe import Markup
from flask.views import MethodView
from flask import request, render_template, redirect, url_for, session, flash

#   Importing CS50 libraries
from cs50 import SQL
from lib.cs50.helpers import login_required, lookup, apology

class StockTrading(MethodView):
    methods = ['GET', 'POST']
    __db__ = SQL('sqlite:///finance.db')

    @login_required
    def get(self):

        #   Ensures the request path
        if request.path == '/': return self.UserPortefolio()
        elif request.path == '/buy': return render_template('buy.html')
        elif request.path == '/sell':
            user = self.__db__.execute('SELECT username, cash FROM users WHERE id = ?', session['user_id'])
            options = self.__db__.execute("SELECT abbrivation FROM ?;", user[0]['username'])

            #   Clear memory
            del user

            return render_template('sell.html', options= options)
        elif request.path == '/quote': return redirect('/')
        elif request.path == '/history': return self.TradingHistory()

        return


    @login_required
    def post(self):

        #   Ensures the request path
        if request.path == '/quote': return self.quote()
        elif request.path == '/sell': return self.SellStocks()
        elif request.path == '/buy': return self.PurchaseShares()

        return redirect(url_for('index.html'))

    @login_required
    def UserPortefolio(self):

        """ Show portfolio of stocks
        #  Execute multiple SELECT
        #   * GROUP,    def StockTrading(): pass BY HAVING, SUM and or WHERE
        #   Call lookup
        """

        #   Selecting the user information | add stock_value to users
        user = self.__db__.execute('SELECT username, cash FROM users WHERE id = ?', int(session['user_id']))


        # Creates a new tables if it doesnt already exists
        self.__db__.execute("""CREATE TABLE IF NOT EXISTS ? (
                                    -- Description :    Track user's investments portefolio
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    abbrivation TEXT NOT NULL,
                                    qty INT NOT NULL,
                                    price REAL NOT NULL,
                                    total REAL NOT NULL,
                                    UNIQUE (abbrivation));""", str(user[0]['username']))


        self.__db__.execute("""CREATE TABLE IF NOT EXISTS trading_history (
                                    --  Description : Track trading history
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    user_id INTEGER NOT NULL,
                                    abbrivation TEXT NOT NULL,
                                    status TEXT NOT NULL DEFAULT UNKOWN,
                                    qty INT NOT NULL,
                                    price REAL NOT NULL,
                                    time_stamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                                    FOREIGN KEY (user_id) REFERENCES users(id));""")

        stock = self.__db__.execute('SELECT qty, abbrivation, total FROM ?;', user[0]['username'])

        if stock:
            for i in stock:
                value = lookup(i['abbrivation'])
                self.__db__.execute('UPDATE ? SET price = ? WHERE abbrivation = ?;', user[0]['username'], value['price'], value['symbol'])
                self.__db__.execute('UPDATE ? SET total = ? WHERE abbrivation = ?;', user[0]['username'], stock[0]['qty'] * value['price'], value['symbol'])

            #   Calculate total value
            total = user[0]['cash']
            for i in stock:
                total += i['total']

            print(total)
            #   Update the users stock value and total value
            self.__db__.execute('UPDATE users SET stock_value = ?, total = ? WHERE id = ?', total - user[0]['cash'], total, session['user_id'])

        return render_template('index.html', userinfo = self.__db__.execute('SELECT * FROM users WHERE id = ?;', session['user_id']), stocks = self.__db__.execute('SELECT * FROM ?;',user[0]['username']), history = self.__db__.execute('SELECT abbrivation, qty, status, price, time_stamp FROM trading_history WHERE user_id = ?;', int(session['user_id'])))

    @login_required
    def TradingHistory(self):

        userinfo = userinfo = self.__db__.execute('SELECT * FROM users WHERE id = ?;', session['user_id'])
        return render_template('index.html', userinfo = self.__db__.execute('SELECT * FROM users WHERE id = ?;', session['user_id']), stocks = self.__db__.execute('SELECT * FROM ?;',userinfo[0]['username']), history = self.__db__.execute('SELECT abbrivation, qty, status, price, time_stamp FROM trading_history WHERE user_id = ?;', int(session['user_id'])))

    @login_required
    def PurchaseShares(self):

        """ Purchase stocks
        #   Require the user to input a stock's symbol, implemented as text field where name is symbol.
        #   *   Render an apology if blank or does not exist
        #   Require user to input number of shares, implemented as a text field whose name is shares.
        #   *   Render an apology if the input is less than zero
        #   Submit the user input through POST -> /buy
        #   redirect user to the homepage
        #   Call lookup to fetch the current price of a stock
        #   Select how much cash the user currently has in users.
        #   Add one or more new tables, to keep track of the purchase. Store enough information
        #   * Use appopriate SQLite types.
        #   *   Define UNIQUE indexes on unique fields
        #   *   Define (non-UNIQUE) indexes on any fields which will be used as a SELECT with WHERE
        #   Render and apology without completing a purchase, if the user cannot afford the number of shares at the current price.
        #   race condition or user trancations is not needed
        """

        #   Initializing databases
        user = self.__db__.execute('SELECT username, cash, stock_value FROM users WHERE id = ?;', session['user_id'])

        try:
            #   Fetch the total price
            share = lookup(request.form['symbol'])

            #   Ensure symbol field is not blank & share exists
            if not request.form['symbol'] or not lookup(request.form['symbol']):
                raise Exception("Blank fields can not be requested / Share Does not exists")

            #   Ensure the user requests a valid quanity
            if not request.form['shares'] or int(request.form['shares']) < 1:
                raise Exception("Minimum one share must be bought")

            #   Ensure the user has enough cash to purchase a share
            if user[0]['cash'] < (int(request.form['shares']) * share['price']): raise Exception(f"You need atlast ${user[0]['cash'] - (int(request.form['shares']) * share['price'])} more to purchase this type of share")

        except Exception as e: return apology(f'{e}', 400)

        #   Updates the transaction history
        self.__db__.execute("INSERT INTO trading_history (user_id, abbrivation, status, qty, price) VALUES (?, ?, ?, ?, ?);", session['user_id'], request.form['symbol'], "BOUGHT", request.form['shares'], share['price'])

        #   Message the user
        flash(Markup(f"You bought <b>{request.form['shares']}</b> of <b>{share['symbol']}</b>, total paid <b>{(int(request.form['shares']) * share['price'])}</b>"))

        #   Ensure the symbol is not already in the users portofolio
        for row in self.__db__.execute('SELECT * FROM ?', user[0]['username']):
            print(row)
            print(self.__db__.execute('SELECT * FROM ?', user[0]['username']))
            if row['abbrivation'] == request.form['symbol']:

                self.__db__.execute("UPDATE ? SET qty = ?, price = ?, total = ? WHERE abbrivation = ?;", user[0]['username'], row['qty'] + int(request.form['shares']),  share['price'], row['total'] + (int(request.form['shares']) * share['price']), request.form['symbol'])

                #   Updates the record with new values
                self.__db__.execute('UPDATE users SET cash = ? WHERE id = ?;', user[0]['cash'] - (int(request.form['shares']) * share['price']), session['user_id'])

                #   Calculate total
                ui = self.__db__.execute('SELECT username, cash, stock_value FROM users WHERE id = ?;', session['user_id'])

                total = ui[0]['cash']
                for i in self.__db__.execute('SELECT total FROM ?', user[0]['username']):
                    total += i['total']

                self.__db__.execute('UPDATE users SET stock_value = ?, total = ? WHERE id = ?;', total - user[0]['cash'], total, session['user_id'])

                #   Clear memory
                del share, ui,

                return render_template('index.html', userinfo= self.__db__.execute('SELECT username, cash, total, stock_value FROM users WHERE id = ?;', session['user_id']),  stocks=self.__db__.execute('SELECT abbrivation, qty, price, total FROM ?;', user[0]['username']), history=self.__db__.execute('SELECT * FROM trading_history WHERE user_id = ?;', int(session['user_id'])))


        #   Inserting a new element into user's portefolio table
        self.__db__.execute("INSERT INTO ? (qty, price, total, abbrivation) VALUES (?,?,?,?);", user[0]['username'], request.form['shares'], share['price'], (int(request.form['shares']) * share['price']), request.form['symbol'])

        #   Updates the record with new values
        self.__db__.execute('UPDATE users SET cash = ? WHERE id = ?;', user[0]['cash'] - (int(request.form['shares'])*share['price']), session['user_id'])

        #   Calculate total
        ui = self.__db__.execute('SELECT username, cash, stock_value FROM users WHERE id = ?;', session['user_id'])
        total = ui[0]['cash']

        for i in self.__db__.execute('SELECT * FROM ?', user[0]['username']):
            total += i['total']

        #   Updates the record with new values
        self.__db__.execute('UPDATE users SET stock_value = ?, total = ? WHERE id = ?;', total - user[0]['cash'], total, session['user_id'])


        #   Clear memory
        del share

        return render_template('index.html', userinfo=self.__db__.execute('SELECT username, cash, total, stock_value FROM users WHERE id = ?;', session['user_id']),  stocks=self.__db__.execute('SELECT  abbrivation, qty, price, total FROM ?;',  user[0]['username']), history=self.__db__.execute('SELECT * FROM trading_history WHERE user_id = ?;', int(session['user_id'])))


    @login_required
    def SellStocks(self):
        ''' Sell stocks
        #   Require the user to input the Stock symbol, implemented as a select menu whose name is symbol
        #   * Render an apology if the user fails to select a stock or if submitted the user does not own any shares of the stock.
        #   Require the user to input a number of shares, implemented as a text field whose name is shares.
        #   *   Render an apology if the input is not greater than zero or if the user does not own x shares.
        #   Submit the user input through POST -> /sell
        #   Redirect the user to the home page
        '''

        #   Initializing databases
        user = self.__db__.execute('SELECT username, cash, stock_value FROM users WHERE id = ?;', session['user_id'])
        stocks = self.__db__.execute('SELECT * FROM ? WHERE abbrivation = ?;', user[0]['username'], request.form['symbol'])

        try:

            #   Ensure the user requests a valid quanity
            if int(request.form['shares']) < 1: raise Exception("Minimum one share must be selected")

            #   Ensure the user has enough shares to sell
            if int(stocks[0]['qty']) < int(request.form['shares']): raise Exception('Can not sell more shares than you have available')

        #   Throw an exception
        except Exception as e: return apology(f'{e}', 400)

        #   Fetch the total price
        share = lookup(request.form['symbol'])
        price = int(request.form['shares']) * share['price']

        #   Updates the transaction history
        self.__db__.execute("INSERT INTO trading_history (user_id, abbrivation, status, qty, price) VALUES (?, ?, ?, ?, ?);", session['user_id'], request.form['symbol'], "SOLD", int(request.form['shares']), share['price'])

        #   Ensure updates the users portofolio
        self.__db__.execute("UPDATE ? SET qty = ?, price = ?, total = ? WHERE abbrivation = ?;", user[0]['username'], stocks[0]['qty'] - int(request.form['shares']), share['price'], stocks[0]['total'] - price, request.form['symbol'])

        #   Ensure every stocks with 0 qanity deletes
        for i in self.__db__.execute('SELECT qty FROM ?', user[0]['username']):
            if int(i['qty']) == 0: self.__db__.execute("DELETE FROM ? WHERE qty = 0;", user[0]['username'])

        #   Calculate total ammount
        ui = self.__db__.execute('SELECT username, cash, stock_value FROM users WHERE id = ?;', session['user_id'])
        total = ui[0]['cash']
        for i in self.__db__.execute('SELECT * FROM ?', user[0]['username']): total += i['total']

        #   Updates the record with new values
        self.__db__.execute('UPDATE users SET cash = ? WHERE id = ?;', user[0]['cash'] + price, session['user_id'],  )

        #   Updates the record with new values
        self.__db__.execute('UPDATE users SET total = ?, stock_value = ? WHERE id = ?;', total, total - user[0]['cash'], session['user_id'],  )

        #   Embeds a message to the user
        flash(Markup(f"You Sold <b>{request.form['shares']}</b><b>{share['symbol']}</b> share, Total paid to your account $<b>{price}</b>"))

        #   Clear memory
        del share, price, stocks, ui
        return render_template('index.html', userinfo= self.__db__.execute('SELECT username, cash, total, stock_value FROM users WHERE id = ?;', session['user_id']),  stocks= self.__db__.execute('SELECT  abbrivation, qty, price, total FROM ?;',  user[0]['username']), history=self.__db__.execute('SELECT * FROM trading_history WHERE user_id = ?;', int(session['user_id'])))

    @login_required
    def quote(self):
        """ Quote stock """

        #   Initalizing databases
        user = self.__db__.execute('SELECT username, cash, total, stock_value FROM users WHERE id = ?;', int(session['user_id']))
        try:
            #   Ensure symbol field is not blank & share exists
            if not request.form['symbol'] or not lookup(request.form['symbol']): raise Exception("Share not found")

        except Exception as e: return apology(f"{e}", 400)
        arg = lookup(request.form['symbol'])

        #   Send the user a message
        flash(Markup(f"A share of {arg['symbol']} costs ${arg['price']}"))
        return redirect('/')
        #return render_template('index.html', userinfo=user,  stocks=self.__db__.execute('SELECT  abbrivation, qty, price, total FROM ?;',  user[0]['username']), history=self.__db__.execute('SELECT * FROM trading_history WHERE user_id = ?;', int(session['user_id'])))


""" Personal touch
#   Allow the user to change their passwords.
#   Allow the users to add additional cash to their account..
#   Allow users to buy more shares or sell shares of stocks they already own via
index itself, without having to type stocks symbol manually
*   Select, buttons
"""
