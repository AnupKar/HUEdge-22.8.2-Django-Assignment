from django.urls import path
from . import views
urlpatterns = [
    path('issue/getAllComments/',views.CommentList.as_view()),
    path('issue/getCommentById/<int:pk>/',views.CommentDetail.as_view())
]