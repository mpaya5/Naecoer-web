from django.urls import path

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path("contact/", views.contact, name="contact"),

]
