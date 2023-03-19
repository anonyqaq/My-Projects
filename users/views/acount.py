from django.shortcuts import render, redirect

def login(request):
    if request.method == "GET":
        return render(request, "login.html")