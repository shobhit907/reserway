from django.urls import path
from . import views

app_name='bookings'

urlpatterns = [
    path('',views.home,name='home'),
    path('book/<int:journey_id>/',views.PassengerDetailsFormPage,name='passenger_details_form'),
    path('admin_release_train/', views.AdminReleaseTrain, name='admin_release_train'),
    path('view_ticket/<int:ticket_id>/',views.viewTicket,name='view_ticket'),
    path('my_tickets/',views.myTickets,name='my_tickets')
]