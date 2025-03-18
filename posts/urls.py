from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)
urlpatterns = [
    path("", PostListView.as_view(), name="posts_list"), 
    path('<int:pk>/',PostDetailView.as_view(), name="posts_detail"), 
    path('create/',PostCreateView.as_view(), name="posts_create"),  
]