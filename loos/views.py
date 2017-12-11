from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect
from .models import Ticket


def index(request):
    context = {}
    return render(request, 'loos/index.html', context)


def ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    context = {
        "id": ticket_id,
        "prize_text": ticket.prize.prize_text,
        'prize_info': ticket.prize.prize_description,
    }
    return render(request, 'loos/ticket.html', context)


def search(request):
    return HttpResponsePermanentRedirect(f"/loos/{request.GET['search']}")
