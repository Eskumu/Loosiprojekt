from django.urls import path, include

from . import views

app_name = 'loos'
urlpatterns = [
    path("", views.index.as_view(), name='index'),
    path("loos/<int:ticket_id>/", views.ticket.as_view(), name="ticket"),
    path("otsing/", views.search, name="search"),
    path("", include('auth.urls'))
]
