#check50 cs50/problems/2024/x/finance
#   Importing responsories
from flask import Flask
from flask_session import Session

#   Importing custom libraries
from lib.views.stocks import StockTrading
from lib.views.acc_mang import ManageAccounts
from lib.config.app_config import DevelopmentConfig


#   Importing cs50 libraries
from lib.cs50.helpers import usd

# Application Configurations
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#   Url rules
app.add_url_rule("/", view_func=StockTrading.as_view(name="index.html"))
app.add_url_rule("/buy", view_func=StockTrading.as_view(name="buy.html"))
app.add_url_rule("/sell", view_func=StockTrading.as_view(name="sell.html"))
app.add_url_rule("/quote", view_func=StockTrading.as_view(name="quote.html"))
app.add_url_rule("/login", view_func=ManageAccounts.as_view(name="login.html"))
app.add_url_rule("/history", view_func=StockTrading.as_view(name="history.html"))
app.add_url_rule("/logout", view_func=ManageAccounts.as_view(name="logout.html"))
app.add_url_rule("/register", view_func=ManageAccounts.as_view(name="register.html"))
app.add_url_rule("/settings", view_func=ManageAccounts.as_view(name="settings.html"))

#   Applying filters
app.jinja_env.filters['usd'] = usd

if __name__ == "__main__":
    app.run()
