from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not "counter" in request.session:
        request.session['counter']=0
    return render(request, "word_gen/index.html")

def create(request):
    context = {
        "unique_id" : get_random_string(32)
    }
    request.session["counter"] += 1
    print(context)
    return render(request, "word_gen/index.html", context)

def reset(request):
    del request.session["counter"]
    return redirect("/")