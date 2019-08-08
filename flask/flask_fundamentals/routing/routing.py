from flask import Flask
app = Flask (__name__)
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def success():
    return "Dojo!"

@app.route("/say/<name>")
def hi(name):
    print(name)
    return f"Hi {name}!"

@app.route("/repeat/<times>/<word>")
def times(times, word):
    # return int(times) * (str(word) + " ")
    # return int(times) * f"{word}" 
    return int(times) * f"{word}"

# @app.route("/default", defaults={"name" : "Art Todorov"})
# @app.route("/default/<name>")
# def default(name):
#     return "then value is: " + name

if __name__ == "__main__":
    app.run(debug=True)