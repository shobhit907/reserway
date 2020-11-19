from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    name = models.TextField()
    age = models.IntegerField(
        validators=[MaxValueValidator(200), MinValueValidator(0)]
    )
    gender = models.CharField(
        max_length=1, choices=[("M", "Male"), ("F", "Female"), ("O", "Other")]
    )

    def __str__(self):
        return self.name

class Ticket (models.Model):
    ticketId = models.AutoField(primary_key=True)
    pnrNumber = models.TextField()
    agent = models.ForeignKey(BookingAgent, on_delete=models.CASCADE, blank = False, null = False)
    passenger1 = models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = True)
    passenger2 = models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = True)
    passenger3 = models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = True)
    passenger4 = models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = True)
    passenger5 = models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = True)
    passenger6 = models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = True)

    def __str__ (self):
        return self.ticketId + " " + self.pnrNumber

class BookingAgent (models.Model):
    agentId = models.AutoField(primary_key=True)
    name = models.TextField()
    creditCardNumber = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.agentId + " " + self.name

class BookingStatus (models.Model):
    journey = models.ForeignKey (TrainSchedule, on_delete=models.CASCADE, blank = False, null = False)
    noOfACSeatsRemaining = models.IntegerField()
    noOfSleeperSeatsRemaining = models.IntegerField()

    def __str__ (self):
        return self.journey.journey_id

class ACBookingStatus (models.Model):
    journey = models.ForeignKey (TrainSchedule, on_delete=models.CASCADE, blank = False, null = False)
    coachNumber = models.TextField()
    seatNumber = models.IntegerField()
    pnrNumber = models.TextField()
    passenger =  models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = False)

    def __str__ (self):
        return self.journey.journey_id + " " + self.coachNumber

class SleeperBookingStatus (models.Model):
    journey = models.ForeignKey (TrainSchedule, on_delete=models.CASCADE, blank = False, null = False)
    coachNumber = models.TextField()
    seatNumber = models.IntegerField()
    pnrNumber = models.TextField()
    passenger =  models.ForeignKey(Passenger, on_delete=models.CASCADE, blank = False, null = False)

    def __str__ (self):
        return self.journey.journey_id + " " + self.coachNumber

class CoachStructureAC (models.Model):
    seatNumber = models.AutoField(primary_key=True)
    seatType = models.TextField()

    def __str__ (self):
        return self.seatNumber + " " + self.seatType

class CoachStructureSleeper (models.Model):
    seatNumber = models.AutoField(primary_key=True)
    seatType = models.TextField()

    def __str__ (self):
        return self.seatNumber + " " + self.seatType