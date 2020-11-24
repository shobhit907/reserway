from django.db import models

# Create your models here.
class Journey(models.Model):
    j_id = models.AutoField(primary_key=True)
    date = models.DateField()
    no_of_stops= models.IntegerField()
    train_name = models.CharField(max_length=30)
    train_id = models.IntegerField()

class Routes(models.Model):
    journey = models.ForeignKey(Journey,on_delete=models.CASCADE)
    station_name = models.CharField(max_length=30)
    stop_number = models.IntegerField()
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()