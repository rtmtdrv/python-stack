from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "This is a secret"

# def display():

# # def create(request):
#     mysql = connectToMySQL("email_db")
#     query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
#     data = {
#              'email': request.form['email']
#            }
#     mysql.query_db(query, data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    is_valid = True
    if len(request.form["email"]) < 1:
        flash("Email cannot be blank!")
        is_valid = False
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address!")
        is_valid = False

    if not is_valid:
        return redirect("/")
    else:
        # flash("The email you entered email is a VALID email address! Thank you!")
        mysql = connectToMySQL("email_db")
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        data = {
            "email": request.form["email"]
        }
        result = mysql.query_db(query, data)
        return redirect("/success/" + str(result))

        
@app.route("/success/<result>")
def success(result):
    # flash("The email you entered (user_email) is a VALID email address! Thank you!")
    mysql = connectToMySQL("email_db") 
    query = ("SELECT * FROM emails WHERE id = %(id)s")
    data = {
        'id' :  result
    }
    user_email = mysql.query_db(query, data)

    mysql = connectToMySQL("email_db") 
    query = ("SELECT * FROM emails")
    emails = mysql.query_db(query)

    return render_template("success.html", email = emails, user_email = user_email)
        
if __name__ == "__main__":
    app.run(debug=True)