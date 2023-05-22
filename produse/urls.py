from django.urls import path

from produse import views

urlpatterns = [
    path('create_ppetrolier/', views.PPetrolierCreateView.as_view(), name="create-ppetrolier"),
    path('list_ppetroliere/',views.PPetrolierListView.as_view(), name="list-ppetroliere"),
]