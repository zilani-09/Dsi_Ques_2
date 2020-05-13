

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
#from . import blogapp


urlpatterns = [
    #path('fisrtapp/', include('fisrtapp.urls')),
    path('admin/', admin.site.urls),
    path('', include('account.urls'),name ='account'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
