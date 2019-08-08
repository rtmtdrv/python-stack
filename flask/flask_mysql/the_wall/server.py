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

    return render_template("logreg.html")

@app.route("/register_validate", methods=["POST"])
def validation():
    error = False
    mysql = connectToMySQL('the_wall_db')
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
        mysql2 = connectToMySQL('the_wall_db')
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
    mysql = connectToMySQL('the_wall_db')
    query = "SELECT * FROM users WHERE email = %(email)s"
    data = {
        "email": request.form["email"]
    }
    result = mysql.query_db(query,data)
    if result:
        if bcrypt.check_password_hash(result[0]["password"], request.form["password"]):
            session["USER_KEY"] = result[0]["id"]
            session["first_name"] = result[0]["first_name"]
            session["last_name"] = result[0]["last_name"]
            return redirect("/wall")

    flash("You could not be logged in", "login_top")
    return redirect("/")

@app.route("/send_message", methods=["POST"])
def send_message():
    mysql = connectToMySQL('the_wall_db')
    query = "SELECT * FROM users WHERE id = %(id)s"
    data = {
        "id":request.form["post_message"]
    }
    users = mysql.query_db(query,data)

    if len(request.form["message"])>250:
        flash("Message is over 250 characters", "send_error")
        return redirect("/wall")
    if len(request.form["message"]) == 0:
        flash("Empty message", "send_error")
        return redirect("/wall") 
    else:      
        mysql = connectToMySQL('the_wall_db')
        query = "INSERT INTO messages (users_id, sent_to_id, message, created_at, updated_at) VALUES (%(user_id)s, %(sent_to_id)s, %(message)s, NOW(), NOW());"
        data = {
            "message": request.form["message"],
            "user_id": session["USER_KEY"],
            "sent_to_id": request.form["post_message"]
        }
        mysql.query_db(query,data)
        flash("Your message to %s %s has been sent" %(users[0]['first_name'].title(), users[0]['last_name'].title()), "msg_success")
        return redirect("/wall")

@app.route("/wall")
def wall_index():
    if not session["USER_KEY"]:
        return redirect("/")

    mysql = connectToMySQL('the_wall_db')
    query = "SELECT messages.id, messages.users_id, messages.sent_to_id, messages.message, messages.created_at, messages.updated_at, users.first_name, users.last_name FROM messages join users on users.id = messages.users_id  WHERE messages.sent_to_id = %(user_id)s ORDER BY messages.created_at desc;"
    data = {
        "user_id": session['USER_KEY']
    }
    message_check = mysql.query_db(query,data)
    # count = 0
    # for i in message_check:
        # count += 1

    mysql2 = connectToMySQL('the_wall_db')
    send_query = "SELECT * FROM users WHERE NOT id = %(user_id)s"
    send_data = {
        "user_id":session["USER_KEY"]
    }
    send_check = mysql2.query_db(send_query,send_data)
    print(send_check)

    mysql3 = connectToMySQL('the_wall_db')
    query = "SELECT * FROM messages WHERE users_id = %(user_id)s"
    data = {
        "user_id": session['USER_KEY']
    }
    user_posts = mysql3.query_db(query,data)
    posts = 0
    for i in user_posts:
        posts += 1
    print(posts)
    return render_template("/wall.html", sends = send_check, messages = message_check, posts = posts)
    # return render_template("/wall.html", sends = send_check, count = count, messages = message_check, posts = posts)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/delete_message/<message_id>")
def del_msg(message_id):
    mysql = connectToMySQL('the_wall_db')
    query = "SELECT * FROM messages where id = %(message_id)s"
    data = {
        "message_id" : message_id
    }
    result = mysql.query_db(query,data)
    session["message_num"] = result[0]["id"]

    if result[0]["sent_to_id"] != session["USER_KEY"]:
        return redirect("/danger")
    elif result[0]["sent_to_id"] == session["USER_KEY"]:
        mysql = connectToMySQL('the_wall_db')
        query = "DELETE FROM messages WHERE id= %(message_id)s"
        data = {
            "message_id":message_id
        }
        mysql.query_db(query,data)
        return redirect("/wall")

@app.route("/danger", methods=["GET"])
def danger():
    session["USER_KEY"] = False
    return render_template("/danger.html")

if __name__=="__main__":
    app.run(debug=True)