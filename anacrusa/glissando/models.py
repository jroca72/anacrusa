# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from decimal import Decimal

# modelos

# Compositor ----------------------------------------------
class compositor(models.Model):
    compositor = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Compositores"

    def __unicode__(self):
        return self.compositor

# Instrumento ---------------------------------------------
class instrumento(models.Model):
    instrumento = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Instrumentos"

    def __unicode__(self):
        return self.instrumento

# Etiqueta ------------------------------------------------
class etiqueta(models.Model):
    etiqueta = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Etiquetas"

    def __unicode__(self):
        return self.etiqueta

# Obra ----------------------------------------------------
class obra(models.Model):
    obra = models.CharField(max_length=200)
    compositor = models.ForeignKey(compositor,default=None, null=False, blank=False)
    fecha = models.DateTimeField(default=datetime.now, blank=False)

    class Meta:
        verbose_name_plural = "Obras"
    
    def __unicode__(self):
        return self.obra 

# Partitura ------------------------------------------------
class partitura(models.Model):
    paritura = models.CharField(max_length=200)
    obra = models.ForeignKey(obra, default=None, null=False, blank=False)
    instrumento = models.ForeignKey(instrumento, default=None, null=False, blank=False)
    anotaciones = models.BooleanField(default=False)
    fecha = models.DateTimeField(default=datetime.now, blank=False)
    fichero = models.FileField(upload_to="partituras/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Partituras"

    def __unicode__(self):
        return self.paritura

# Tag -------------------------------------------------------
class tag(models.Model):
    obra = models.ForeignKey(obra, default=None, null=False, blank=False)
    etiqueta = models.ForeignKey(etiqueta, default=None, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Tags"

    def __unicode__(self):
        return self.obra

