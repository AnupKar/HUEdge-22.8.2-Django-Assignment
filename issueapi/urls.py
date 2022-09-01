from django.urls import path
from . import views
urlpatterns = [
    path('getissues/', views.getData),
]