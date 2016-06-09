# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Categoria(models.Model):
    nom = models.CharField(verbose_name="Nom", max_length=20, help_text="El nom de la categoria del producte.")

    def __unicode__(self):
        return u'%s' % (self.nom)

class Fabricant(models.Model):
    nom = models.CharField(verbose_name="Nom", max_length=20, help_text="El nom del fabricant del producte.")

    def __unicode__(self):
        return u'%s' % (self.nom)

class Producte(models.Model):
    nom = models.CharField(verbose_name="Nom", max_length=20, help_text="El nom del producte.")
    preu = models.DecimalField(verbose_name="Preu", max_digits=5, decimal_places=2, help_text="El preu del producte.")
    quantitat = models.PositiveIntegerField(verbose_name="Stock", help_text="La quantitat d'existències.")
    resum = models.TextField(verbose_name="Resum", max_length=1000, help_text="El resum del producte.")
    descripcio = models.CharField(verbose_name="Descripció", max_length=100, help_text="La descripció del producte.")
    categories = models.ManyToManyField(Categoria, verbose_name="Categoria", help_text="La categoria del producte.")
    fabricant = models.ForeignKey(Fabricant, verbose_name="Fabricant", help_text="El fabricant del producte.")
    imatge = models.ImageField(verbose_name="Imatge", upload_to='i_logo', height_field=None, width_field=None, max_length=100, help_text="La imatge del producte.")
    video = models.CharField(verbose_name="Demostració", max_length=150, null=True, blank=True, help_text="La demostració mitjançant una URL d'un vídeo.")

    class Meta:
        unique_together = [('nom', 'fabricant')]

    def mostra_categories(self):
        return u", ".join([c.nom for c in self.categories.all()])

    def mostra_categories_id(self):
        return u", ".join([unicode(c.id) for c in self.categories.all()])

    def __unicode__(self):
        return u'%s' % (self.nom)