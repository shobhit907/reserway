from django.shortcuts import render
from .forms import PassengerDetailsForm
from django.http import HttpResponseRedirect
from .models import * 

# Create your views here.

def home(request):
    return render(request,'bookings/home.html')


def PassengerDetailsFormPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PassengerDetailsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            passenger1 = Passenger.objects.create(name=form.cleaned_data['passenger1Name'],age=form.cleaned_data['passenger1Age'],gender=form.clean_data['passenger1gender'])
            if form.cleaned_data['passenger2Name']!=NULL and form.cleaned_data['passenger2Age']!=NULL and form.cleaned_data['passenger2gender']!=NULL:
                passenger2 = Passenger.objects.create(name=form.cleaned_data['passenger2Name'],age=form.cleaned_data['passenger2Age'],gender=form.clean_data['passenger2gender'])
            else:
                passenger2=null
            if form.cleaned_data['passenger3Name']!=NULL and form.cleaned_data['passenger3Age']!=NULL and form.cleaned_data['passenger3gender']!=NULL:
                passenger3 = Passenger.objects.create(name=form.cleaned_data['passenger3Name'],age=form.cleaned_data['passenger3Age'],gender=form.clean_data['passenger3gender'])
            else:
                passenger3=null
            if form.cleaned_data['passenger4Name']!=NULL and form.cleaned_data['passenger4Age']!=NULL and form.cleaned_data['passenger4gender']!=NULL:
                passenger4 = Passenger.objects.create(name=form.cleaned_data['passenger4Name'],age=form.cleaned_data['passenger4Age'],gender=form.clean_data['passenger4gender'])
            else:
                passenger4=null
            if form.cleaned_data['passenger5Name']!=NULL and form.cleaned_data['passenger5Age']!=NULL and form.cleaned_data['passenger5gender']!=NULL:
                passenger5 = Passenger.objects.create(name=form.cleaned_data['passenger5Name'],age=form.cleaned_data['passenger5Age'],gender=form.clean_data['passenger5gender'])
            else:
                passenger5=null
            if form.cleaned_data['passenger6Name']!=NULL and form.cleaned_data['passenger6Age']!=NULL and form.cleaned_data['passenger6gender']!=NULL:
                passenger6 = Passenger.objects.create(name=form.cleaned_data['passenger6Name'],age=form.cleaned_data['passenger6Age'],gender=form.clean_data['passenger6gender'])
            else:
                passenger6=null

            ba=request.user.booking_agent
            # Generate passenger id and store to passenger table
            # generate pnr and store pnr + passenger id to tickets table
            #Booking Agent from: request.user
            # call stored procedure to get seat type 
            # call trigger to update remaining seats
            # redirect to new page displaying ticket and then further options
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PassengerDetailsForm()

    return render(request, 'bookings/passenger_details_form.html', {'form': form})

