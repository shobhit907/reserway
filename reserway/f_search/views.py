from django.shortcuts import render
from .models import *
from .forms import *
import datetime
# Create your views here.

def search_direct(s,d,flag,min_time=datetime.datetime(1,1,1)):
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
    
    # print(s3)
    # print(d3)
    t4=[]
    for element1 in s3:
        for element2 in d3:
            print("Element=")
            print(element1,element2)
            if flag==0 and element1.journey.j_id==element2.journey.j_id and element1.stop_number<element2.stop_number:
                t4.append(element1.journey)
            else:
                print("Rejected1")
            if flag==1 and element1.journey.j_id==element2.journey.j_id and element1.stop_number<element2.stop_number and element1.departure_time>min_time:
                t4.append(element1.journey)
            else:
                print("Rejected2")
    # print("Results:")
    # for element in t4:
    #     print(element.j_id,element.date,element.train_name)
    return t4

def DisplaySearchForm(request):
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            s=form.cleaned_data['source']
            d=form.cleaned_data['destination']
            
            # s2=Routes.objects.raw('SELECT * from f_search_routes')
            # d2=Routes.objects.raw('SELECT * from f_search_routes')
            # s3=[]
            # for element in s2:
            #     if element.station_name==s:
            #         s3.append(element)
            # d3=[]
            # for element in d2:
            #     if element.station_name==d:
            #         d3.append(element)
            
            # # print(s3)
            # # print(d3)
            # t4=[]
            # for element1 in s3:
            #     for element2 in d3:
            #         if element1.journey.j_id==element2.journey.j_id and element1.stop_number<element2.stop_number:
            #             t4.append(element1.journey)
            # # print("Results:")
            # # for element in t4:
            # #     print(element.j_id,element.date,element.train_name)
            t4=search_direct(s,d,0)
            print("Single:")
            for element in t4:
                print(element.j_id,element.date,element.train_name)

            so2=Routes.objects.raw('SELECT * from f_search_routes')
            do2=Routes.objects.raw('SELECT * from f_search_routes')
            so3=[]
            for element in so2:
                if element.station_name==s:
                    so3.append(element)
            do3=[]
            for element in do2:
                if element.station_name==d:
                    do3.append(element)


            ino2=[]
            so5=[]
            print(so3)
            for element in so3:
                jour=element.journey.j_id
                sno=element.stop_number
                # print(jour)
                # print(sno)
                so4=Routes.objects.raw('SELECT * from f_search_routes')
                for item in so4:
                    if item.journey.j_id==jour and item.stop_number>sno:
                        so5.append(item)
            print("This:")
            for element in so5:
                print(element.station_name,element.arrival_time)
            t5=[]
            for element in so5:
                print("Called")
                temp=search_direct(element.station_name,d,1,element.arrival_time)
                if len(temp)>0:
                    nl=[element,temp]
                    t5.append(nl)
            print("Here")
            for item in t5:
                for over_item in item[1]:
                    if item[0].journey.j_id!=over_item.j_id:
                        print(s,item[0].journey.train_name,item[0].station_name,over_item.train_name,d)
    else:
        form=SearchForm()

    return render(request,'f_search/train_search.html',{'form':form})