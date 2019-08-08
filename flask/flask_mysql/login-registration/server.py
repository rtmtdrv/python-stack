from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "Its a secret"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

USER_KEY = "user_id"

@app.route("/")
def index():
    # if USER_KEY not in session:
    #     session[USER_KEY] = False

    return render_template("login_register.html")

@app.route("/register_validate", methods=["POST"])
def validation():
    error = False
    mysql = connectToMySQL('login_reg_db')
    query = "SELECT * FROM users WHERE email = %(email)s"
    data = {
        "email":request.form["email"]
    }
    check = mysql.query_db(query, data)

    # if len(request.form["first_name"]) == 0 or len(request.form["last_name"]) == 0 or len(request.form["email"]) == 0 or len(request.form["password"]) or len(request.form["confirm_password"]) == 0:
    #     flash("All input fields are required", "top")
    #     error=True
    # else:
    if not NAME_REGEX.match(request.form["first_name"]):
        flash("First name field cannot contain numbers", "frname")
        error=True

    if len(request.form["first_name"]) < 2:
        flash("First name length too short", "")
        error=True

    if len(request.form["last_name"]) < 2:
        flash("Last name length too short")
        error=True
    
    if not NAME_REGEX.match(request.form["last_name"]):
        flash("Last name field cannot contain numbers", "last_name")
        error=True

    if len(check) > 0:
        flash("Email has already been registered", "email")
        error=True

    if not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email format", "email")
        error=True

    if request.form["password"] != request.form["confirm_password"]:
        flash("Passwords do not match", "password")
        error=True

    if error == True:
        return redirect("/")
    if error == False:
        req_pass_hash = bcrypt.generate_password_hash(request.form["password"])
        mysql2 = connectToMySQL('login_reg_db')
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(frname)s, %(lsname)s, %(em)s, %(pass)s, NOW(), NOW());"
        data = {
            "frname" : request.form["first_name"],
            "lsname" : request.form["last_name"],
            "em" : request.form["email"],
            "pass" : req_pass_hash
        }
        new_user = mysql2.query_db(query,data)
        session[USER_KEY] = new_user
        flash("Successful Registration! Thank you for registering, you may now log in", "success")
        return redirect('/')

@app.route("/login", methods=["POST"])
def login():
    mysql = connectToMySQL('login_reg_db')
    query = "SELECT * FROM users WHERE email = %(email)s"
    data = {
        "email": request.form["email"]
    }
    result = mysql.query_db(query,data)
    if result:
        if bcrypt.check_password_hash(result[0]["password"], request.form["password"]):
            session["USER_KEY"] = result[0]["id"]
            session["first_name"] = result[0]["first_name"]
            return redirect("/home")

    flash("You could not be logged in", "login_top")
    return redirect("/")

@app.route("/home")
def home_index():
    if not session["USER_KEY"]:
        return redirect("/")
    else:
        return render_template("/home.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)