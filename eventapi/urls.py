from django.urls import path
from . import views
urlpatterns = [
    path('issue/event/',views.EventClass.as_view()),
    #path('issue/getCommentById/<int:pk>/',views.CommentDetail.as_view())
]