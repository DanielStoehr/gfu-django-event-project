from django.shortcuts import render
from django.views.generic import TemplateView
from events.models import Event


class HomePageView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context.update({"top_events": Event.objects.all()[:10]})
        return context
