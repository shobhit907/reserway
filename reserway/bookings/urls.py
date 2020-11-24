from django.urls import path
from . import views

app_name='bookings'

urlpatterns = [
    path('',views.home,name='home'),
    path('passenger_details_form/',views.PassengerDetailsFormPage,name='passenger_details_form'),
    path('ticket_page/', views.DisplayTicketPage, name='ticket_page'),
]