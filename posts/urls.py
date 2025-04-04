from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    create_comment
)
urlpatterns = [
    path("", PostListView.as_view(), name="posts_list"), 
    path('<int:pk>/',PostDetailView.as_view(), name="posts_detail"), 
    path('create/',PostCreateView.as_view(), name="posts_create"), 
    path('update/<int:pk>/', PostUpdateView.as_view(), name="post_update"), 
    path("create_comment/", create_comment, name="comment_create"),
]