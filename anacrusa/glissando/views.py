# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.generic import ListView, DetailView
from glissando.models import compositor, instrumento, etiqueta, obra, partitura, tag

# Create your views here.
def home(request):

	obras = obra.objects.order_by('fecha')
	context = {'las_obras': obras}
	return render(request, 'glissando/home.html', context)
    