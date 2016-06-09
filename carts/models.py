# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Comanda(models.Model):
    comanda_id = models.AutoField(primary_key=True)
    usuari = models.ForeignKey(User)
    data = models.DateField(auto_now=True)
    carrer = models.CharField(verbose_name="Carrer", max_length=50, help_text="El nom del carrer on enviarem la comanda.")
    poblacio = models.CharField(verbose_name="Població", max_length=30, help_text="La població a la qual pertany el carrer.")
    codi_postal = models.PositiveIntegerField(verbose_name="Codi Postal", help_text="El codi postal de la població.")
    provincia = models.CharField(verbose_name="Província", max_length=30, help_text="La província a la qual pertany la població.")
    estats = (('T', 'Tramitant-se'),
              ('E', 'Enviat')
              )
    estat = models.CharField(max_length=1, choices=estats, default='T')

class Linia(models.Model):
    linia_id = models.AutoField(primary_key=True)
    comanda_id = models.ForeignKey('Comanda')
    producte_id = models.ForeignKey('items.Producte')
    preu = models.DecimalField(max_digits=5, decimal_places=2)
    quantitat = models.PositiveIntegerField()