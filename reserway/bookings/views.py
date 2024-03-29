from django.shortcuts import render,reverse
from .forms import PassengerDetailsForm,SearchTrainsForm
from django.http import HttpResponseRedirect,HttpResponse
import datetime,time
from django.http import JsonResponse
from .models import TrainSchedule,BookingStatus
from django.shortcuts import render
from .forms import PassengerDetailsForm,TrainScheduleForm
from .models import * 
import datetime

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
            context['trains']=[]
            for row in obj:
                li=[row.journey_id,row.train.id,row.train.train_name,BookingStatus.objects.get(journey__journey_id=row.journey_id).noOfACSeatsRemaining,BookingStatus.objects.get(journey__journey_id=row.journey_id).noOfSleeperSeatsRemaining,row.journey_date,row.train.source_station,row.train.dest_station]
                context['trains'].append(li)
    form=SearchTrainsForm()
    context['form']=form
    return render(request,'bookings/home.html',context)


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


def PassengerDetailsFormPage(request,journey_id):
    if request.method == 'POST':
        form = PassengerDetailsForm(request.POST)
        if form.is_valid():
            p_count=1
            j_id=journey_id
            p1 = Passenger.objects.create(name=form.cleaned_data['passenger1Name'],age=form.cleaned_data['passenger1Age'],gender=form.cleaned_data['passenger1Gender'])
            p2=p3=p4=p5=p6=None
            if form.cleaned_data['passenger2Name']!=None and form.cleaned_data['passenger2Age']!=None and form.cleaned_data['passenger2Gender']!=None:
                p2 = Passenger.objects.create(name=form.cleaned_data['passenger2Name'],age=form.cleaned_data['passenger2Age'],gender=form.cleaned_data['passenger2Gender'])
                p_count+=1
            if form.cleaned_data['passenger3Name']!=None and form.cleaned_data['passenger3Age']!=None and form.cleaned_data['passenger3Gender']!=None:
                p3 = Passenger.objects.create(name=form.cleaned_data['passenger3Name'],age=form.cleaned_data['passenger3Age'],gender=form.cleaned_data['passenger3Gender'])
                p_count+=1
            if form.cleaned_data['passenger4Name']!=None and form.cleaned_data['passenger4Age']!=None and form.cleaned_data['passenger4Gender']!=None:
                p4 = Passenger.objects.create(name=form.cleaned_data['passenger4Name'],age=form.cleaned_data['passenger4Age'],gender=form.cleaned_data['passenger4Gender'])
                p_count+=1
            if form.cleaned_data['passenger5Name']!=None and form.cleaned_data['passenger5Age']!=None and form.cleaned_data['passenger5Gender']!=None:
                p5 = Passenger.objects.create(name=form.cleaned_data['passenger5Name'],age=form.cleaned_data['passenger5Age'],gender=form.cleaned_data['passenger5Gender'])
                p_count+=1
            if form.cleaned_data['passenger6Name']!=None and form.cleaned_data['passenger6Age']!=None and form.cleaned_data['passenger6Gender']!=None:
                p6 = Passenger.objects.create(name=form.cleaned_data['passenger6Name'],age=form.cleaned_data['passenger6Age'],gender=form.cleaned_data['passenger6Gender'])
                p_count+=1
            
            ba=request.user.booking_agent
            
            seat = BookingStatus.objects.get(journey__journey_id=j_id)
            pnr=str(int(datetime.datetime.now().timestamp()))
            ticket=None
            if form.cleaned_data['seat_type']=="AC":
                current_bookings=seat.noOfACSeatsRemaining
                if current_bookings<p_count:
                    #cannot book
                    return HttpResponseRedirect('')
                else:
                    BookingStatus.objects.filter(journey__journey_id=j_id).update(noOfACSeatsRemaining=current_bookings-p_count)
                    ticket = Ticket.objects.create(journey=TrainSchedule.objects.get(journey_id=journey_id),seat_type="AC",pnrNumber=pnr,booking_agent=ba,passenger1=p1,passenger2=p2,passenger3=p3,passenger4=p4,passenger5=p5,passenger6=p6)
                    for itr in range (0,p_count):
                        coach_number=int((current_bookings+17)/18)
                        if current_bookings%18==0:
                            seat_number=18
                        else:
                            seat_number=current_bookings%18
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
                        ACBookingStatus.objects.create(journey=TrainSchedule.objects.get(journey_id=j_id),coachNumber=coach_number,seatNumber=seat_number,ticket=ticket,passenger=passen)

            elif form.cleaned_data['seat_type']=="Sleeper":
                current_bookings=seat.noOfSleeperSeatsRemaining
                if current_bookings<p_count:
                    #cannot book
                    return HttpResponseRedirect('')
                else:
                    BookingStatus.objects.filter(journey__journey_id=j_id).update(noOfSleeperSeatsRemaining=current_bookings-p_count)
                    ticket = Ticket.objects.create(journey=TrainSchedule.objects.get(journey_id=journey_id),seat_type="Sleeper",pnrNumber=pnr,booking_agent=ba,passenger1=p1,passenger2=p2,passenger3=p3,passenger4=p4,passenger5=p5,passenger6=p6)
                    for itr in range (0,p_count):
                        coach_number=int((current_bookings+17)/18)
                        if current_bookings%18==0:
                            seat_number=18
                        else:
                            seat_number=current_bookings%18
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
                        SleeperBookingStatus.objects.create(journey=TrainSchedule.objects.get(journey_id=j_id),coachNumber=coach_number,seatNumber=seat_number,ticket=ticket,passenger=passen)

            return HttpResponseRedirect('/view_ticket/{}'.format(ticket.ticketId))

    else:
        form = PassengerDetailsForm()

    return render(request, 'bookings/passenger_details_form.html', {'form': form,'journey_id':journey_id})

def viewTicket(request,ticket_id):
    context={}
    ticket=Ticket.objects.get(ticketId=ticket_id)
    if ticket.booking_agent.user.username!=request.user.username:
        context['permission']=False
    else:
        context['permission']=True
        context['ticket']=ticket
    return render(request,'bookings/ticket.html',context)
