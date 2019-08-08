from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Secret Key"

def setSession():
    session["random_num"] = random.randint(1, 100)

@app.route("/")
def index():
    if session["random_num"] == None:
        setSession()
    else:
        pass

    if "message" not in session:
        session["message"]=""

    print(session['random_num'])
    return render_template("index.html", message=session['message'])

@app.route("/guess", methods=["GET","POST"])
def askUserForNumber():
    guess = int(request.form["number"])
    if guess == session["random_num"]:
        session["message"] = "Correct"
    elif guess > session["random_num"]:
        session["message"] = "Too High"
    else:
        session["message"] = "Too Low"
    print(guess)
    return redirect("/")

@app.route("/reset", methods=["GET", "POST"])
def reset():
    setSession()
    session.pop("message")

    return redirect("/")

if __name__== "__main__":
    app.run(debug=True)