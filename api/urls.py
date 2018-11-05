from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter
from rest_framework import renderers

from api.views import TiposClienteViewSet, TiposDocumentoViewSet,Suma, api_root

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'tipos-cliente', views.TiposClienteViewSet)
router.register(r'tipos-documento', views.TiposDocumentoViewSet)
router.register(r'estatus', views.EstatusViewSet)

# API URLS
urlpatterns = [
    path('', views.api_root),
    path('suma/',views.Suma.as_view(),
         name='suma'),
    path('', include(router.urls)),
]



# Se agrega para que el Browsable API pueda tener un Login incorporado
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]