from django.shortcuts import render, redirect
from .models import *
from time import strftime, strptime

def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        "all_shows" : Show.objects.all(),
    }
    return render(request, "tv_shows_app/index.html", context)

def display_show(request, show_id): 
    show_info = Show.objects.get(id=show_id)
    time_format = show_info.release_date.strftime("%b %d, %Y")
    context = {
        "show_info_html" : show_info,
        "release_date_html" : time_format
    }
    return render(request, "tv_shows_app/viewshow.html", context)

def add_show(request):
    new_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["release_date"], description = request.POST["description"])
    new_show_id = new_show.id

    return redirect(f"/shows/{new_show_id}")

def new_show(request):
    return render(request, "tv_shows_app/addshow.html")

def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    time_format = show.release_date.strftime("%Y-%m-%d")
    context = {
        "show_html" : show,
        "release_date_html" : time_format
    }

    return render(request, "tv_shows_app/editshow.html", context)

def update_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST["title"]
    show.network = request.POST["network"]
    show.release_date = request.POST["release_date"]
    show.description = request.POST["description"]
    show.save()
    return redirect(f"/shows/{show_id}")

def remove_show(request, show_id):
    show= Show.objects.get(id=show_id)
    show.delete()

    return redirect("/shows")

