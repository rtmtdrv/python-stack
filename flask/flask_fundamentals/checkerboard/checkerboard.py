from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", times=5, column=8)

@app.route('/<x>')
def row(x):
    return render_template("index.html", times=int(x), column=8)

@app.route('/<x>/<y>')
def row_column(x, y):
    return render_template("index.html", times=int(x), column=int(y))

if __name__ == "__main__":
    app.run(debug=True)