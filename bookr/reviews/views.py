from django.shortcuts import render

def index(request):
    name = "Django"
    return render(request, 'base.html', {"name": name})
