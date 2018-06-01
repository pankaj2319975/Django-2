from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^paperbank/', include('paperbank.urls')),
    #url(r'^paperbank/computer/', include('paperbank.urls')),
    #url(r'^paperbank/electronics/', include('paperbank.urls')),
    #url(r'^paperbank/it/', include('paperbank.urls')),
    #url(r'^paperbank/biotech/', include('paperbank.urls')),
    #url(r'^paperbank/bca/', include('paperbank.urls')),
    #url(r'^paperbank/mech/', include('paperbank.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    ]
