from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info", methods=["POST"])
def create_info():
    is_valid = True
    if len(request.form["name"]) < 1:
        is_valid = False
        flash("Please enter a name")
    if len(request.form["location"]) < 1:
        is_valid = False
        flash("Please enter a name")
    if len(request.form["language"]) < 1:
        is_valid = False
        flash("Please enter a name")
    if len(request.form["comment"]) < 1:
        is_valid = False
        flash("Please enter a comment")

    if not is_valid:
        return redirect("/")
    else:
        flash("Successfully added!")
        return render_template("show.html", name_submitted = request.form["name"], location_submitted = request.form["location"], language_submitted = request.form["language"], comments_submitted = request.form["comment"])

if __name__ == "__main__":
    app.run(debug=True)