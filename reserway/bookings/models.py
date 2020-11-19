from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import BookingAgent

# Create your models here.
class Train(models.Model):
    id = models.AutoField(primary_key=True)
    train_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + "  " + self.train_name


class TrainSchedule(models.Model):
    journey_id = models.AutoField(primary_key=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE, blank=False, null=False)
    journey_date = models.DateTimeField(blank=False, null=False)
    num_ac_coaches = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)], default=10
    )
    num_sleeper_coaches = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)], default=10
    )

    def __str__(self):
        return (
            self.train.train_name
            + "  "
            + str(self.journey_date.strftime("%d/%m/%Y, %H:%M:%S"))
        )


class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=[MaxValueValidator(200), MinValueValidator(1)]
    )
    gender = models.CharField(
        max_length=1, choices=[("M", "Male"), ("F", "Female"), ("O", "Other")]
    )

    def __str__(self):
        return self.name

class Ticket (models.Model):
    ticketId = models.AutoField(primary_key=True)
    pnrNumber = models.CharField(max_length=12)
    booking_agent = models.ForeignKey(BookingAgent, on_delete=models.CASCADE, blank = False, null = False,related_name='tickets')
    passenger1 = models.OneToOneField(Passenger, on_delete=models.CASCADE, blank = False, null = True,related_name='ticket1')
    passenger2 = models.OneToOneField(Passenger, on_delete=models.CASCADE, blank = False, null = True,related_name='ticket2')
    passenger3 = models.OneToOneField(Passenger, on_delete=models.CASCADE, blank = False, null = True,related_name='ticket3')
    passenger4 = models.OneToOneField(Passenger, on_delete=models.CASCADE, blank = False, null = True,related_name='ticket4')
    passenger5 = models.OneToOneField(Passenger, on_delete=models.CASCADE, blank = False, null = True,related_name='ticket5')
    passenger6 = models.OneToOneField(Passenger, on_delete=models.CASCADE, blank = False, null = True,related_name='ticket6')

    def __str__ (self):
        return str(self.ticketId) + " " + self.pnrNumber


class BookingStatus (models.Model):
    journey = models.ForeignKey (TrainSchedule, on_delete=models.CASCADE, blank = False, null = False)
    noOfACSeatsRemaining = models.IntegerField()
    noOfSleeperSeatsRemaining = models.IntegerField()

    def __str__ (self):
        return self.journey.journey_id

class ACBookingStatus (models.Model):
    journey = models.ForeignKey (TrainSchedule, on_delete=models.CASCADE, blank = False, null = False)
    coachNumber = models.CharField(max_length=5)
    seatNumber = models.IntegerField()
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE,blank=False,null=False)
    passenger =  models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = False)

    def __str__ (self):
        return str(self.journey.journey_id) + " " + self.coachNumber

class SleeperBookingStatus (models.Model):
    journey = models.ForeignKey (TrainSchedule, on_delete=models.CASCADE, blank = False, null = False)
    coachNumber = models.CharField(max_length=5)
    seatNumber = models.IntegerField()
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE,blank=False,null=False)
    passenger =  models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = False)

    def __str__ (self):
        return str(self.journey.journey_id) + " " + self.coachNumber

class CoachStructureAC (models.Model):
    seatNumber = models.IntegerField()
    seatType = models.CharField(max_length=2)

    def __str__ (self):
        return str(self.seatNumber) + " " + self.seatType

class CoachStructureSleeper (models.Model):
    seatNumber = models.IntegerField()
    seatType = models.CharField(max_length=2)

    def __str__ (self):
        return str(self.seatNumber) + " " + self.seatType