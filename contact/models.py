from django.db import models

# Create your models here.


class Mesaj(models.Model):
    full_nume =models.CharField(max_length=50,null=False)
    email=models.EmailField(null=False)
    telefon = models.CharField(max_length=20, null=False)
    mesaj = models.TextField(null=False)


