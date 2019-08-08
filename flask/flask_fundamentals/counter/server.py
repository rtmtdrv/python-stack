from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def index():
    if "count" in session:
        session["count"] = session["count"] + 1
    else:
        session["count"] = 0
    return render_template("index.html", count = session["count"])

@app.route("/destroy_session", methods=["POST"])
def refresh():
    session.pop("count")
    return redirect ("/")

@app.route("/increment", methods=["POST"])
def increment_by_two():
    session["count"] += 1
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)