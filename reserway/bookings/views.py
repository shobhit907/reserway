from django.shortcuts import render,reverse
from .forms import PassengerDetailsForm,SearchTrainsForm
from django.http import HttpResponseRedirect,HttpResponse
import datetime,time
from django.http import JsonResponse
from .models import TrainSchedule
# Create your views here.

def home(request):
    context={}
    if request.method=='POST':
        form=SearchTrainsForm(request.POST)
        if form.is_valid():
            source_station=form.cleaned_data['source_station']
            dest_station=form.cleaned_data['dest_station']
            doj=form.cleaned_data['date_of_journey']
            obj=TrainSchedule.objects.all()
            if source_station is not None:
                obj=obj.filter(train__source_station__name=source_station)
            if dest_station is not None:
                obj=obj.filter(train__dest_station__name=dest_station)
            obj=obj.filter(journey_date__gte=doj).order_by('journey_date')
            print(source_station,dest_station,doj)
            context['query']=form.cleaned_data
            context['trains']=obj
    form=SearchTrainsForm()
    context['form']=form
    return render(request,'bookings/home.html',context)


def PassengerDetailsFormPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PassengerDetailsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PassengerDetailsForm()

    return render(request, 'bookings/passenger_details_form.html', {'form': form})
