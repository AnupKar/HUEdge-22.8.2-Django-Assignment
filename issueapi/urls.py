from django.urls import path
from . import views
urlpatterns = [
    path('issue/getissues/', views.IssueDetails.as_view()),
]