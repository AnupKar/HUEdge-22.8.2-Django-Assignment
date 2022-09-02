from django.urls import path
from . import views

urlpatterns = [
    path('project/getdata/', views.ProjectList.as_view()),
    path('project/getProjectDetail/', views.ProjectDetails.as_view()),
    path('project/getProjectById/<int:pk>/', views.ProjectDetailById.as_view()),
    path('project/getdata/<str:title>/', views.getByTitle),
    #path('project/deleteProject/<int:id>/', views.deleteProject),
    #path('project/updateProject/<int:id>/', views.updateProjetcDetail),
    path('project/createProject/', views.CreateProject.as_view()),
    path('project/ProjectByItem/', views.ProjectList.as_view()),
]