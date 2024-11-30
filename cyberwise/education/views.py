from django.shortcuts import render 
from .models import Module

# Create your views here.
def home(request):
    modules = Module.objects.all()
    return render(request, 'education/home.html', {'modules': modules})

def detail(request, id):
    module = Module.objects.get(id=id)
    return render(request, 'education/detail.html', {'module': module})
