from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def contact_page(request):
    return HttpResponse("Hello Lumee!!")

def contacts(request):
    list_contacts = {
        "contacts":[
            {
                "nume": "Catinean",
                "prenume": "Avram",
                "functia": "Manager",
                "email": "catinean.avram@cucu.com",
                "tel": 40744520260
            },
            {
                "nume": "Catinean",
                "prenume": "Maria",
                "functia": "Secretara",
                "email": "catinean.maria@cucu.com",
                "tel": 40744520262
            },
            {
                "nume": "Catinean",
                "prenume": "Andrei",
                "functia": "Tehnician",
                "email": "catinean.andrei@cucu.com",
                "tel": 40744520261
            },
            {
                "nume": "Bog",
                "prenume": "Cristian",
                "functia": "Casier",
                "email": "bug.cristian@cucu.com",
                "tel": 40744520263
            },
        ]
    }

    return render(request, "contact/contact_page.html", list_contacts)

def manager_details(request):
    manager = {
        "manager_details": [
            {
                "nume": "Catinean",
                "prenume": "Avram",
                "functia": "Manager",
                "email": "catinean.avram@cucu.com",
                "tel": 40744520260
            }
        ]
    }
    return render(request, "contact/manager_details.html", manager)


def secretara_details(request):
    secretara = {
        "secretara_details": [
            {
                "nume": "Catinean",
                "prenume": "Maria",
                "functia": "Secretara",
                "email": "catinean.maria@cucu.com",
                "tel": 40744520262
            }
        ]
    }
    return render(request, "contact/secretara_details.html", secretara)


def tehnician_details(request):
    tehnician = {
        "tehnician_details": [
            {
                "nume": "Catinean",
                "prenume": "Andrei",
                "functia": "Secretara",
                "email": "catinean.andrei@cucu.com",
                "tel": 40744520261
            }
        ]
    }
    return render(request, "contact/tehnician_details.html", tehnician)

def casier_details(request):
    casier = {
        "casier_details": [
            {
                "nume": "Bog",
                "prenume": "Cristian",
                "functia": "Casier",
                "email": "bug.cristian@cucu.com",
                "tel": 40744520263
            }
        ]
    }
    return render(request, "contact/casier_details.html", casier)

class ContactTemplateView(TemplateView):
    template_name = 'contact/contact_button.html'