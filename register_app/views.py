from django.shortcuts import render
from .models import User

def home(request):
    users = User.objects.all()
    return render(request, "register_app.html", {"users": users})

def save(request):
    nameUser = request.POST.get("name")
    User.objects.create(name=nameUser)
    users = User.objects.all()
    return render(request, "register_app.html", {"users": users})