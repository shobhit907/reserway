from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Names
# Create your views here.

def index(request):
    if request.method=="POST":
        input_name=request.POST['input-name']
        if(len(input_name)>0):
            na=Names(name=input_name)
            na.save()
            print("Saved")
            return HttpResponseRedirect(reverse('testApp:all'))

    return render(request,"testApp/index.html")

def all(request):
    obj=Names.objects.all()
    context={'all_names':obj}
    return render(request,"testApp/all_names.html",context)


