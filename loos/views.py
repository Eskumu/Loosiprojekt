from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect
from django.views.generic import TemplateView, DetailView

from .models import Ticket


class index(LoginRequiredMixin ,TemplateView):
    template_name = 'loos/index.html'


class ticket(LoginRequiredMixin, DetailView):
    model = Ticket
    pk_url_kwarg = 'ticket_id'
    context_object_name = 'ticket'
    template_name = 'loos/ticket.html'



def search(request):
    return HttpResponsePermanentRedirect(f"/loos/{request.GET['search']}")
