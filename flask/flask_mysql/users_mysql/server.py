from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/users")
def index():
    mysql = connectToMySQL("user_db")
    user = mysql.query_db('SELECT * FROM users;')

    return render_template("users.html", all_users = user)

@app.route("/users/new")
def new_user():
    return render_template("add_user.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    mysql = connectToMySQL("user_db")
    query = "INSERT INTO users(first_name, last_name, email) VALUES (%(fn)s, %(ln)s, %(email)s)"
    data = {
        "fn" : request.form["fn_name"],
        "ln" : request.form["ln_name"],
        "email" : request.form["email"]
    }
    user_id = mysql.query_db(query, data)
    return redirect('/user/' + str(user_id))

@app.route("/user/<user_id>")
def show(user_id):
    mysql = connectToMySQL("user_db")
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        'id' : user_id
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template('show.html', user = user)

@app.route('/user/<user_id>/edit')
def show_edit(user_id):
    mysql = connectToMySQL("user_db")
    query = "SELECT * FROM users WHERE id =%(id)s;"
    data = {
        "id" : user_id
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template('edit.html', user = user)

@app.route("/edit_user/<user_id>", methods=["POST"])
def update_user(user_id):
    mysql = connectToMySQL("user_db")
    query = "UPDATE users SET first_name = %(fn)s, last_name = %(ln)s, email = %(email)s WHERE id = %(id)s;"
    data = {
        "fn" : request.form['f_name'],
        "ln" : request.form['l_name'],
        "email" : request.form['email'],
        "id" : user_id
    }
    user = mysql.query_db(query, data)
    print(user)
    return redirect('/user/' + user_id)

@app.route('/delete/<user_id>')
def delete(user_id):
    mysql = connectToMySQL("user_db")
    query = "DELETE FROM users WHERE ID = %(id)s;"
    data = {
        'id' : user_id
    }
    user = mysql.query_db(query, data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
