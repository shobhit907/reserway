from django.shortcuts import render
from .models import *
from .forms import *
import datetime
# Create your views here.

def DisplaySearchForm(request):
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            s=form.cleaned_data['source']
            d=form.cleaned_data['destination']
            
            s2=Routes.objects.raw('SELECT * from f_search_routes')
            d2=Routes.objects.raw('SELECT * from f_search_routes')
            s3=[]
            for element in s2:
                if element.station_name==s:
                    s3.append(element)
            d3=[]
            for element in d2:
                if element.station_name==d:
                    d3.append(element)
            
            print(s3)
            print(d3)
            t4=[]
            for element1 in s3:
                for element2 in d3:
                    if element1.journey.j_id==element2.journey.j_id and element1.stop_number<element2.stop_number:
                        t4.append(element1.journey)
            print("Results:")
            for element in t4:
                print(element.j_id,element.date,element.train_name)


    else:
        form=SearchForm()

    return render(request,'f_search/train_search.html',{'form':form})