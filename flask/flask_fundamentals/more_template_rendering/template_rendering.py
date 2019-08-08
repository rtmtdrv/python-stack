from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/lists')
def render_lists():
    student_info = [
        {'name' : 'Michael', 'age' : 35}
        {'name' : 'John', 'age' : 30}
        {'name' : 'Mark', 'age' : 25}
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random)