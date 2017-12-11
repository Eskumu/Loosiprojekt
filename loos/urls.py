from django.urls import path

from . import views

app_name = 'loos'
urlpatterns = [
    path("", views.index, name='index'),
    path("loos/<int:ticket_id>/", views.ticket, name="ticket"),
    path("otsing/", views.search, name="search"),
]
