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
                t4.append((element1, element2))
            else:
                print("Rejected1")
            if flag==1 and element1.journey.j_id==element2.journey.j_id and element1.stop_number<element2.stop_number and element1.departure_time>min_time:
                t4.append((element1, element2))
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
            context = {}
            t4=search_direct(s,d,0)
            context['direct_routes'] = []
            print("Single:")
            i = 1
            for element in t4:
                if (element != None):
                    context['direct_routes'].append((i, element[0], element[1]))
                    print(element[0].journey.j_id,element[0].journey.date,element[0].journey.train_name)

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
                        so5.append((element, item))
            print("This:")
            for element in so5:
                print(element[1].station_name,element[1].arrival_time)
            t5=[]
            for element in so5:
                print("Called")
                temp=search_direct(element[1].station_name,d,1,element[1].arrival_time)
                if len(temp)>0:
                    nl=[element[0], element[1], temp]
                    t5.append(nl)
            i = 1
            print("Here")
            context['break_routes'] = []
            for item in t5:
                for over_item in item[2]:
                    if item[1].journey.j_id!=over_item[1].journey.j_id:
                        context['break_routes'].append((i, item[0], item[1], over_item[0], over_item[1]))
                        print(s,item[1].journey.train_name,item[1].station_name,over_item[1].journey.train_name,d)
            return render(request, 'f_search/results.html', context)
    else:
        form=SearchForm()

    return render(request,'f_search/train_search.html',{'form':form})