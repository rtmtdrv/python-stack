from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "log_reg_app/index.html")

def register_user(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/")
        else:
            hash1 = bcrypt.hashpw(request.POST["pw"].encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name=request.POST["fname"], last_name=request.POST["lname"], email=request.POST["email"], pw_hash=hash1)
            request.session["userid"] = new_user.id
            messages.success(request, "Successful Registration or Login")
            return redirect("/success")
    return redirect("/")

def success(request):
    if not "userid" in request.session:
        messages.error(request, "You are not logged in.")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session["userid"])
        context = {
            "user_html": user
        }
        return render(request, "log_reg_app/success.html", context)

def login(request):
    email_match = User.objects.get(email=request.POST["email"])
    if bcrypt.checkpw(request.POST["pw"].encode(), email_match.pw_hash.encode()):
        request.session["userid"] = email_match.id
        messages.success(request, "Successfully logged in!")
        return redirect("/success")
    else: messages.error(request, "Incorrect password.")
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")



