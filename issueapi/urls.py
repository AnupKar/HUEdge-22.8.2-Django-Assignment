from django.urls import path
from . import views
urlpatterns = [
    path('issue/getissues/', views.IssueDetails.as_view()),
    path('issue/getIssueData', views.IssueData.as_view()),
    path('issue/getIssueById/<int:id>/', views.IssueDetailById.as_view()),
]