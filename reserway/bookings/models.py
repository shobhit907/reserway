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
    age = models.IntegerField()
    gender = models.CharField(
        max_length=1, choices=[("M", "Male"), ("F", "Female"), ("O", "Other")]
    )

    def __str__(self):
        return self.name
