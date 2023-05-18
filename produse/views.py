from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


class ProduseTemplateView(TemplateView):
    template_name = 'categorii/categorii.html'
