from django.urls import path

from produse import views

urlpatterns = [
    path('create_ppetrolier/', views.PPetrolierCreateView.as_view(), name="create-ppetrolier"),
    path('list_ppetroliere/',views.PPetrolierListView.as_view(), name="list-ppetroliere"),

    path('create_pcuratenie/',views.PCuratenieCreateView.as_view(), name="create-pcuratenie"),
    path('list_pcuratenie/',views.PCuratenieListView.as_view(), name="list-pcuratenie"),

    path('create_pconsumabil/',views.PConsumabilCreateView.as_view(), name="create-pconsumabil"),
    path('list_pconsumabile/',views.PConsumabileListView.as_view(), name="list-pconsumabile"),
]