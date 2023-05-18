from django.db import models

class ProdusPetrolier(models.Model):

    nume_produs = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    pret = models.FloatField(max_length=6)
    detalii_produs = models.TextField(max_length=100)
