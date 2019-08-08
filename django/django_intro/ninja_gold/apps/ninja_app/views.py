from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime


# Create your views here.
def index(request):
    if "total" not in request.session:
        request.session["total"] = 0
    if "activity" not in request.session:
        request.session["activity"] = []
    return render(request, "ninja_app/index.html")

def process_money(request):
    activity = []
    if request.POST["building"] == "farm":
        earned = random.randrange(10, 20)
        request.session["total"] += earned
        activity.append('Earned {} from the casino! ({})'.format(earned, strftime("%Y-%m-%d %H:%M %p", gmtime())))
    if request.POST["building"] == "cave":
        earned = random.randrange(5, 10)
        request.session["total"] += earned
        activity.append('Earned {} from the cave! ({})'.format(earned, strftime("%Y-%m-%d %H:%M %p", gmtime())))
    if request.POST["building"] == "house":
        earned = random.randrange(2, 5)
        request.session["total"] += earned
        activity.append('Earned {} from the house! ({})'.format(earned, strftime("%Y-%m-%d %H:%M %p", gmtime())))
    if request.POST["building"] == "casino":
        earned = random.randrange(-50, 50)
        request.session["total"] += earned
        activity.append('Earned {} from the casino! ({})'.format(earned, strftime("%Y-%m-%d %H:%M %p", gmtime())))
    
    request.session["activity"] += activity
    return redirect("/")

def reset(request):
    del request.session["activity"]
    del request.session["total"]
    return redirect("/")
