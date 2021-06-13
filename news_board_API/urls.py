from django.urls import path
from . import views
from .views import Comment_list, Post_list, Post_detail, Comment_detail, vote_view

urlpatterns = [
    path("posts/", Post_list.as_view()),
    path("posts/<int:pk>", Post_detail.as_view()),
    path("comments/", Comment_list.as_view()),
    path("comments/<int:pk>", Comment_detail.as_view()),
    path("posts/<int:question_id>/upvote/", view=vote_view, name="vote_view"),
]
