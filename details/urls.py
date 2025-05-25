from django.contrib import admin
from django.urls import path
from details.views import *

urlpatterns = [
    path("",home,name="home"),
    path("home/",home,name="home"),
    path("about/", about, name="about"),
    path("project/",projects, name="projects"),
    path("certificates/",certificates, name="certificates"),
    path("contact/",contact, name="contact"),
    path("resume/",resume,name="resume")
]
