from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    return HttpResponse("Hey there!!!")

def all(request):
    obj=models.Names.objects.all()
    context={'all_names':obj}
    return render(request,"testApp/all_names.html",context)


