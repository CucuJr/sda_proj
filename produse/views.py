from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from produse.forms import PPetrolierForm, PCuratenieForm, PConsumabilForm
from produse.models import PPetrolier, PCuratenie, PConsumabil


# aici am creat clasele pt creerea si vizualizarea produselor de tip petroliere
class PPetrolierCreateView(CreateView):
    template_name = "categorii/create_ppetroliere.html"
    model = PPetrolier
    form_class = PPetrolierForm
    success_url = reverse_lazy("list-ppetroliere")


class PPetrolierListView(ListView):
    template_name = "categorii/list_ppetroliere.html"
    model = PPetrolier
    context_object_name = "all_ppetroliere"


# aici am creat clasele pt creerea si vizualizarea produselor de tip curatenie
class PCuratenieCreateView(CreateView):
    template_name = "categorii/create_pcuratenie.html"
    model = PCuratenie
    form_class = PCuratenieForm
    success_url = reverse_lazy("list-pcuratenie")

class PCuratenieListView(ListView):
    template_name = "categorii/list_pcuratenie.html"
    model = PCuratenie
    context_object_name = "all_pcuratenie"



# aici am creat clasele pt creerea si vizualizarea produselor de tip consumabile
class PConsumabilCreateView(CreateView):
    template_name = "categorii/create_pconsumabil.html"
    model = PConsumabil
    form_class = PConsumabilForm
    success_url = reverse_lazy("list-pconsumabile")

class PConsumabileListView(ListView):
    template_name = "categorii/list_pconsumabile.html"
    model = PConsumabil
    context_object_name = "all_pconsumabile"