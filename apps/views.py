from django.shortcuts import render,get_object_or_404
from .models import App

def home(request):
    apps = App.objects.all()
    return render(request,'home.html',{'apps':apps})

def app_detail(request,id):
    app = get_object_or_404(App,id=id)
    return render(request,'app.html',{'app':app})
