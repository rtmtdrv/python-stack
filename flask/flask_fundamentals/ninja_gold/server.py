from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "Secret Key"

# def randomNum(start, end):
    # num = random.randrange(start, end)
    # return num

def earn_or_add():
    chance = random.randrange(0, 2)
    if chance == 1:
        return True
    else:
        return False

def addActivity(num, action, location):
    timestamp = datetime.datetime.now()
    if location == "casino":
        if action == "earned":
            earned = "Earned %d from the casino! (%s)" % (num, timestamp)
            session["activity"].insert(0,["won", earned])
        elif action == "lost":
            lost = "Entered a casino and lost %d gold... Ouch... (%s)" % (num, timestamp)
            session["activity"].insert(0, ["lost", lost])
        else:
            print("error")
    elif location == "farm":
        session["activity"].insert(0, ["won", "Earned %d from the %s! (%s)" % (num, location, timestamp)])
    elif location == "cave":
        session["activity"].insert(0, ["won", "Earned %d from the %s! (%s)" % (num, location, timestamp)])
    elif location == "house":
        session["activity"].insert(0, ["won", "Earned %d from the %s! (%s)" % (num, location, timestamp)])
    else:
        print("error")
        
@app.route("/")
def index():
    if "total" not in session:
        session["total"] = 0
    if "activity" not in session:
        session["activity"] = []
    return render_template("index.html", total_gold=session["total"], activities=session["activity"])

@app.route("/process_money", methods=["POST"])
def process_money():
    if request.form["building"] == "farm":
        earned = random.randrange(10, 20)
        session["total"] += earned
        addActivity(earned, 'earned', 'farm')
        
    if request.form["building"] == "cave":
        earned = random.randrange(5, 10)
        session["total"] += earned
        addActivity(earned, 'earned', 'cave')

    if request.form["building"] == "house":
        earned = random.randrange(2, 5)
        session["total"] += earned
        addActivity(earned, 'earned', 'house')

    if request.form["building"] == "casino":
        earned = random.randrange(0, 50)
        chance = earn_or_add()
        if chance == True:
            session["total"] += earned
            addActivity(earned, 'earned', 'casino')
        elif chance == False:
            session["total"] -= earned
            addActivity(earned, 'lost', 'casino')
        else:
            print("error")

    print(earned)
    # print(chance)
    
    return redirect('/')

@app.route('/clear', methods=["POST"])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
        app.run(debug=True)