from django.urls import path
from . import views

app_name='bookings'

urlpatterns = [
    path('',views.home,name='home')
]