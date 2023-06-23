from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from .models import Ticket
from .schema import TicketIn, TicketOut

api = NinjaAPI()


@api.get("/{int:ticket_id}", response=TicketOut)
def get_single_ticket(request, ticket_id):
    obj = get_object_or_404(Ticket, pk=ticket_id)
    return obj


@api.get("/async", response=list[TicketOut])
async def tickets_async(request):
    # qs = Ticket.objects.all() #
    tickets = [ticket async for ticket in Ticket.objects.all()]
    return tickets


@api.get("/", response=list[TicketOut])
def get_all_tickets(request):
    return Ticket.objects.all()


@api.post("/", response=TicketOut)
def create_ticket(request, payload: TicketIn):
    payload_dict = payload.dict()
    ticket = Ticket(**payload_dict)
    ticket.full_clean()
    ticket.save()
    return ticket
