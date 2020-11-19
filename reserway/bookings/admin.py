from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Train)
# admin.site.register(TrainSchedule)
# admin.site.register(Passenger)

from django.apps import apps

app = apps.get_app_config('bookings')

for model_name, model in app.models.items():
    admin.site.register(model)