from django.shortcuts import render
from .forms import PassengerDetailsForm
from django.http import HttpResponseRedirect

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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PassengerDetailsForm()

    return render(request, 'bookings/passenger_details_form.html', {'form': form})

