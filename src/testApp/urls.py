from django.urls import path
from . import views

app_name='testApp'
urlpatterns = [
    path('',views.index),
    path('all/',views.all)
]