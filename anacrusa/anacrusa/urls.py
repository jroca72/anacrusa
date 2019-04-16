
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from glissando import views
from glissando.views import home, partituras

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^$', views.home, name='home'),
     url(r'^partituras/(?P<id_obra>[0-9]+)/$', views.partituras , name = 'partituras'),
]

if settings.DEBUG:
     urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

