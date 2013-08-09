from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'gainedtime.views.vista_inicio', name='vista_inicio'),
	url(r'^login/$', 'gainedtime.views.vista_login', name='vista_login'),
	url(r'^logout/$', 'gainedtime.views.vista_logout', name='vista_logout'),
	url(r'^privado/$', 'gainedtime.views.privado', name='privado'),
	url(r'^menu/$', 'gainedtime.views.vista_menu', name='vista_menu'),
	url(r'^mapa/$', 'gainedtime.views.vista_mapa', name='vista_mapa'),
	url(r'^mesas/$', 'gainedtime.views.lista_mesas', name='lista_mesas'),
	url(r'^mesa/(?P<id_mesa>\d+)$','gainedtime.views.detalle_mesa', name='detalle_mesa'),
	url(r'^cartas/$', 'gainedtime.views.vista_cartas', name='vista_cartas'),
	url(r'^receta/(?P<id_receta>\d+)$','gainedtime.views.detalle_receta', name='detalle_receta'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}),
)
