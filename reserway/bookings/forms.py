from django import forms
from .models import Station, Train

class AdminReleaseTrainForm(forms.Form):
    all_trains=Train.objects.all()
    train = forms.ModelChoiceField(queryset=all_trains,blank=False,required=True)
    journey_date=forms.DateField(widget=forms.widgets.DateTimeInput(attrs={"type":"date"}))
    num_ac_coaches = forms.IntegerField(max_value=100, min_value=0,required=True)
    num_sleeper_coaches = forms.IntegerField(max_value=100, min_value=0,required=True)

class PassengerDetailsForm(forms.Form):
    seat_type= forms.ChoiceField(label="Seat type:", choices=[("AC", "AC"), ("Sleeper", "Sleeper")])
    passenger1Name = forms.CharField(label='Passenger 1 Name:', max_length=100)
    passenger1Age = forms.IntegerField(label='Pasenger 1 Age:', max_value=200, min_value=0)
    passenger1Gender = forms.ChoiceField(label="Passenger 1 Gender:", choices=[("M", "Male"), ("F", "Female"), ("O", "Other")])
    passenger2Name = forms.CharField(label='Passenger 2 Name:', max_length=100, required=False)
    passenger2Age = forms.IntegerField(label='Pasenger 2 Age:', max_value=200, min_value=0, required=False)
    passenger2Gender = forms.ChoiceField(label="Passenger 2 Gender:", choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], required=False)
    passenger3Name = forms.CharField(label='Passenger 3 Name:', max_length=100, required=False)
    passenger3Age = forms.IntegerField(label='Pasenger 3 Age:', max_value=200, min_value=0, required=False)
    passenger3Gender = forms.ChoiceField(label="Passenger 3 Gender:", choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], required=False)
    passenger4Name = forms.CharField(label='Passenger 4 Name:', max_length=100, required=False)
    passenger4Age = forms.IntegerField(label='Pasenger 4 Age:', max_value=200, min_value=0, required=False)
    passenger4Gender = forms.ChoiceField(label="Passenger 4 Gender:", choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], required=False)
    passenger5Name = forms.CharField(label='Passenger 5 Name:', max_length=100, required=False)
    passenger5Age = forms.IntegerField(label='Pasenger 5 Age:', max_value=200, min_value=0, required=False)
    passenger5Gender = forms.ChoiceField(label="Passenger 5 Gender:", choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], required=False)
    passenger6Name = forms.CharField(label='Passenger 6 Name:', max_length=100, required=False)
    passenger6Age = forms.IntegerField(label='Pasenger 6 Age:', max_value=200, min_value=0, required=False)
    passenger6Gender = forms.ChoiceField(label="Passenger 6 Gender:", choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], required=False)

class SearchTrainsForm(forms.Form):
    all_stations=Station.objects.all()
    source_station=forms.ModelChoiceField(queryset=all_stations,blank=True,required=False)
    dest_station=forms.ModelChoiceField(queryset=all_stations,blank=True,required=False)
    date_of_journey=forms.DateField(widget=forms.widgets.DateTimeInput(attrs={"type":"date"}))