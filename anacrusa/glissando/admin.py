# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from glissando.models import compositor, instrumento, etiqueta
from glissando.models import obra, partitura, tag

admin.site.register(compositor)
admin.site.register(instrumento)
admin.site.register(etiqueta)
admin.site.register(obra)
admin.site.register(partitura)
admin.site.register(tag)
 

