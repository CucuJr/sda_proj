from django.urls import path

from contact import views

urlpatterns = [
    path('contact_page/', views.contact_page, name="contact-page"),
    path('contacts/', views.contacts, name="contacts"),
    path('manager_details/', views.manager_details, name="manager-details"),
    path("secretara_details/", views.secretara_details, name="secretara-details"),
    path("tehnician_details/", views.tehnician_details, name="tehnician-details"),
    path("casier_details/", views.casier_details, name="casier-details"),
    path("contact_button/", views.ContactTemplateView.as_view(), name="contact-button"),
    path("mesaj/", views.InregistrareMesaj.as_view(), name="inregistrare-mesaj"),

]