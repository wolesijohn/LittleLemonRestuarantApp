from django.urls import path
from . import views

urlpatterns=[
    path('restaurant/',views.index,name='index')
]