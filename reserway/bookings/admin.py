from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Train)
admin.site.register(TrainSchedule)
admin.site.register(Passenger)