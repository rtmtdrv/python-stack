from flask import Flask, render_template
app = Flask (__name__)

@app.route('/play')
def playground():
    return render_template("index.html", num_times = 3)

@app.route('/play/<times>')
def playground2(times):
    return render_template("index.html", num_times = int(times))

@app.route('/play/<times>/<color>')
def playground3(times, color):
    return render_template("index.html", num_times = int(times), colorselect=color)
    
if __name__ == "__main__":
    app.run(debug=True)