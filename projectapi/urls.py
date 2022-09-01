from django.urls import path
from . import views

urlpatterns = [
    path('project/getdata/', views.getData),
    path('project/getProjectDetail/', views.getProjetcDetail),
    path('project/getdata/<str:title>/', views.getByTitle),
    path('project/deleteProject/<int:id>/', views.deleteProject),
    path('project/updateProject/<int:id>/', views.updateProjetcDetail),
    path('project/createProject/', views.CreateProject.as_view()),
]