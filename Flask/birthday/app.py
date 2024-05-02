#   Title           BirthDays
#
#   Description     A webpage that displays birthdayss using SQL
#
#   Date Started    Wedensday, 17th, April, 2024

#   Importing responsories

from cs50 import SQL
from flask import Flask, jsonify, redirect, render_template, request

# Application Configurations
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["THREADED"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure database connection
sql = SQL("sqlite:///birthdays.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():

    #   Initializing const variables
    __DATA__ = sql.execute("SELECT * FROM birthdays ORDER BY id;")
    #   Initializing classes

    if request.is_json:
        if FormProcessing(request.get_json()) == True:
            return 'Succsessfully transfered data'


        return f'{FormProcessing(request.get_json())}'

    if request.method == "POST":

        #   Insert a record to the database
        if request.form.get('add_record'):
            try:
                if RecordData(request.form.get('name').split(' '), request.form.get('bday').split('-')) != True: raise Exception(RecordData(request.form.get('name').split(' '), request.form.get('bday').split('-')))
            except Exception as e:return render_template("index.html", message='Couldn\'t record data in database', msg=e, entries=__DATA__)
            return render_template("index.html", message="Data successfully recorded in the database", entries=__DATA__)

        #   Remove a record from the database
        elif request.form.get('del_record'):

            try :sql.execute("DELETE FROM birthdays WHERE id=?;", int(request.form.get('del_record')))
            except Exception as e: return render_template("index.html", msg=f"An error Occured with the database {e}")
            return render_template("index.html", entries=sql.execute('SELECT * FROM birthdays ORDER BY id;'))

        elif request.form.get('update'): return render_template("index.html", entries=sql.execute('SELECT * FROM birthdays ORDER BY id;'))
        elif request.form.get('ORDER_bday'): return render_template("index.html", entries= sql.execute("SELECT * FROM birthdays ORDER BY birthday;"))
        elif request.form.get('ORDER_name'): return render_template("index.html", entries=sql.execute("SELECT * FROM birthdays ORDER BY name;"))

    return render_template("index.html", entries=__DATA__)

def RecordData(name, bday):

    try:

        if not name: raise Exception('Name is missing')

        for i in sql.execute('SELECT * FROM birthdays;'):
            if i['name'] == name and bday == i['birthday']: raise Exception(f'The name and birthday can not be equal to an exsisting record')

        for i in name:
            if not str(i).isalpha(): raise Exception('One or more characters are not alphabetic character ')

    except Exception as e: return e

    # Insert the user's entry into the database
    sql.execute(f"INSERT INTO birthdays (name, birthday) VALUES(?, ?);", request.form.get('name'), request.form.get('bday'))
    sql.execute('SELECT * FROM birthdays ORDER BY id;')

    #   Clear variables
    del name,bday

    return True

def FormProcessing(JsonData):

    if JsonData['btn_name'] == 'update':

        try:
            #   Validating the name
            for i in str(JsonData['updated_name']).split(' '):
                if not i.isalpha(): raise Exception(f'A name consist of alphabetic characters')

            for i in sql.execute('SELECT * FROM birthdays;'):
                if i['name'] == JsonData['updated_name'] and int(i['id']) != int(JsonData['id']): raise Exception(f'{JsonData['updated_name']} Already Exists in the database')
                elif i['name'] == JsonData['updated_name'] and int(i['id']) == int(JsonData['id']) and i['birthday'] == JsonData['updated_bday']: raise Exception(f' Data was not modified therefore database not updated')

            #   Validating the birthdays
            bday = str(JsonData['updated_bday']).split('-')

            if not str(JsonData['updated_bday']).split('-'): raise Exception ('Birthdays has to be seperated with "-')
            for i in bday:
                if not i.isdigit(): raise Exception ('Birthdays can only contain numeric values and seperated with "/"')

        except Exception as e: return e

        #   Update values in the database
        sql.execute("UPDATE birthdays SET birthday = ? WHERE id = ?;", JsonData['updated_bday'], int(JsonData['id']))
        sql.execute("UPDATE birthdays SET name = ? WHERE id = ?;", JsonData['updated_name'], int(JsonData['id']))

        #   Clear Memory
        del bday
        del JsonData

        return "Data has been successfully processed !", redirect('/')
    return

if __name__=='__main__':
    app.run()
