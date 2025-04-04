from django.urls import path
from .views import home, about, contact_view

urlpatterns = [
    path("", home, name="root"),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact_view, name="contact")
]