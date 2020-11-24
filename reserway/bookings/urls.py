from django.urls import path
from . import views

app_name='bookings'

urlpatterns = [
    path('',views.home,name='home'),
    path('book/<int:journey_id>/',views.PassengerDetailsFormPage,name='passenger_details_form'),
    path('view_ticket/<int:ticket_id>/',views.viewTicket,name='view_ticket'),
]