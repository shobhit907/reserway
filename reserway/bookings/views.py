from django.shortcuts import render
from .forms import PassengerDetailsForm,TrainScheduleForm
from django.http import HttpResponseRedirect
from .models import * 
import datetime

# Create your views here.
def home(request):
    return render(request,'bookings/home.html')


def TrainJourneyFormPage(request):
    if request.method == 'POST':
        form = TrainScheduleForm(request.POST)
        if form.is_valid():
            t_name=forms.cleaned_data['train_name']
            date=forms.cleaned_data['journey_date']
            ac=forms.cleaned_data['num_ac_coaches']
            sl=forms.cleaned_data['num_sleeper_coaches']

            new_train=TrainSchedule.objects.create(train=t_name,journey_date=date,num_ac_coaches=ac,num_sleeper_coaches=sl)
            j_id=new_train.journey_id
            BookingStatus.objects.create(journey=j_id,noOfACSeatsRemaining=ac*18,noOfSleeperSeatsRemaining=sl*24)
        
        return HttpResponseRedirect('')

    else:
        form = TrainScheduleForm()

    return render(request, 'bookings/train_journey.html', {'form': form})


def PassengerDetailsFormPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PassengerDetailsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            p_count=1
            j_id=forms.cleaned_data['journey_id']
            p1 = Passenger.objects.create(name=form.cleaned_data['passenger1Name'],age=form.cleaned_data['passenger1Age'],gender=form.clean_data['passenger1gender'])
            if form.cleaned_data['passenger2Name']!=NULL and form.cleaned_data['passenger2Age']!=NULL and form.cleaned_data['passenger2gender']!=NULL:
                p2 = Passenger.objects.create(name=form.cleaned_data['passenger2Name'],age=form.cleaned_data['passenger2Age'],gender=form.clean_data['passenger2gender'])
                p_count+=1
            else:
                p2=null
            if form.cleaned_data['passenger3Name']!=NULL and form.cleaned_data['passenger3Age']!=NULL and form.cleaned_data['passenger3gender']!=NULL:
                p3 = Passenger.objects.create(name=form.cleaned_data['passenger3Name'],age=form.cleaned_data['passenger3Age'],gender=form.clean_data['passenger3gender'])
                p_count+=1
            else:
                p3=null
            if form.cleaned_data['passenger4Name']!=NULL and form.cleaned_data['passenger4Age']!=NULL and form.cleaned_data['passenger4gender']!=NULL:
                p4 = Passenger.objects.create(name=form.cleaned_data['passenger4Name'],age=form.cleaned_data['passenger4Age'],gender=form.clean_data['passenger4gender'])
                p_count+=1
            else:
                p4=null
            if form.cleaned_data['passenger5Name']!=NULL and form.cleaned_data['passenger5Age']!=NULL and form.cleaned_data['passenger5gender']!=NULL:
                p5 = Passenger.objects.create(name=form.cleaned_data['passenger5Name'],age=form.cleaned_data['passenger5Age'],gender=form.clean_data['passenger5gender'])
                p_count+=1
            else:
                p5=null
            if form.cleaned_data['passenger6Name']!=NULL and form.cleaned_data['passenger6Age']!=NULL and form.cleaned_data['passenger6gender']!=NULL:
                p6 = Passenger.objects.create(name=form.cleaned_data['passenger6Name'],age=form.cleaned_data['passenger6Age'],gender=form.clean_data['passenger6gender'])
                p_count+=1
            else:
                p6=null

            ba=request.user.booking_agent
            # generate pnr and store pnr + passenger id to tickets table
            
            #Booking Agent from: request.user
            # call stored procedure to get seat type 


            seat = BookingStatus.objects.get(journey=j_id)
            
            if form.cleaned_data['seat_type']=="AC":
                current_bookings=seat.noOfACSeatsRemaining
                if current_bookings<p_count:
                    #cannot book
                    return HttpResponseRedirect('')
                else:
                    BookingStatus.objects.filter(journey=j_id).update(noOfACSeatsRemaining=current_bookings-p_count)
                    ticket = Ticket.objects.create(pnrNumber=int(datetime.datetime.now()),booking_agent=ba,passenger1=p1,passenger2=p2,passenger3=p3,passenger4=p4,passenger5=p5,passenger6=p6)
                    for itr in range (0,p_count):
                        coach_number=(current_bookings/18)+1
                        seat_number=current_bookings%18+1
                        current_bookings-=1
                        if itr==0:
                            passen=p1
                        if itr==1:
                            passen=p2
                        if itr==2:
                            passen=p3
                        if itr==3:
                            passen=p4
                        if itr==4:
                            passen=p5
                        if itr==5:
                            passen=p6
                        ACBookingStatus.objects.create(journey=j_id,coachNumber=coach_number,seatNumber=seat_number,ticket=ticket,passenger=passen)



            if form.cleaned_data['seat_type']=="Sleeper":
                current_bookings=seat.noOfSleeperSeatsRemaining
                if current_bookings<p_count:
                    #cannot book
                    return HttpResponseRedirect('')
                else:
                    BookingStatus.objects.filter(journey=forms.cleaned_data['journey_id']).update(noOfSleeperSeatsRemaining=current_bookings-p_count)
                    ticket = Ticket.objects.create(pnrNumber=int(datetime.datetime.now()),booking_agent=ba,passenger1=p1,passenger2=p2,passenger3=p3,passenger4=p4,passenger5=p5,passenger6=p6)
                    for itr in range (0,p_count):
                        coach_number=(current_bookings/24)+1
                        seat_number=current_bookings%24+1
                        current_bookings-=1
                        if itr==0:
                            passen=p1
                        if itr==1:
                            passen=p2
                        if itr==2:
                            passen=p3
                        if itr==3:
                            passen=p4
                        if itr==4:
                            passen=p5
                        if itr==5:
                            passen=p6
                        SleeperBookingStatus.objects.create(journey=j_id,coachNumber=coach_number,seatNumber=seat_number,ticket=ticket,passenger=passen)

            # redirect to new page displaying ticket and then further options
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PassengerDetailsForm()

    return render(request, 'bookings/passenger_details_form.html', {'form': form})

