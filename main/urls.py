from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Serve other template pages by filename, e.g. /about.html -> main/templates/about.html
    path('<path:page>', views.flatpage, name='flatpage'),
    path("contact/", views.contact_view, name="contact"),
    
]