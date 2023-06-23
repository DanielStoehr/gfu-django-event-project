from typing import Literal

from ninja import ModelSchema

from .models import Ticket


class TicketIn(ModelSchema):
    class Config:
        model = Ticket
        model_fields = "name", "status", "price"
        model_call_clean = True


class TicketOut(ModelSchema):
    class Config:
        model = Ticket
        model_fields = "__all__"
