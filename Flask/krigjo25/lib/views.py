#   Import responsories
from flask.views import MethodView
from flask import render_template, request, flash

class Index(MethodView):

    #   Initialize methods and database
    methods = ["GET", "POST"]

    def get(self): return render_template("index.html")

    def post(self): pass