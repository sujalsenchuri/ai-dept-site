from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("admission/", views.admission, name="admission"),
    path("clubs/", views.clubs, name="clubs"),
    path("news/", views.news, name="news"),

    # Serve other template pages by filename, e.g. /about.html
    path("<path:page>", views.flatpage, name="flatpage"),
]