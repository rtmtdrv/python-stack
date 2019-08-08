from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info", methods=["POST"])
def create_info():
    # print("*"*50)
    # print(request.form)
    # name_from_form = request.form["name"]
    # location_from_form = request.form["location"]
    # language_from_form = request.form["language"]
    # comments_from_form = request.form["message"]
    return render_template("show.html", name_submitted = request.form["name"], location_submitted = request.form["location"], language_submitted = request.form["language"], comments_submitted = request.form["message"])

if __name__ == "__main__":
    app.run(debug=True)