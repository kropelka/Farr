from django.contrib import admin
from .models import Miejscowosc, Adres, Osoba, Firma, Telefon

# Register your models here.
for m in [Miejscowosc, Adres, Osoba, Firma, Telefon]:
    admin.site.register(m)
