from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_list_view, name="news_list"),
]