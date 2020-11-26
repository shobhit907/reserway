from django.urls import path
from . import views

app_name='f_search'

urlpatterns = [
    path('',views.DisplaySearchForm,name='train search')
]