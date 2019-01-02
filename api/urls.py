from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter
from rest_framework import renderers

from api.views import TiposMonedaViewSet, TiposClienteViewSet, TiposDocumentoViewSet,Suma

# Swagger Documentation
from rest_framework_swagger.views import get_swagger_view





# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'tipos-cliente', views.TiposClienteViewSet)
router.register(r'tipos-documento', views.TiposDocumentoViewSet)
router.register(r'tipos-moneda', views.TiposMonedaViewSet)
router.register(r'estatus', views.EstatusViewSet)

# API URLS
urlpatterns = [
    path('suma/',views.Suma.as_view(),
         name='suma'),
    path('', include(router.urls)),
]

# Se agrega para que el Browsable API pueda tener un Login incorporado
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

# Se agregar las URLs para el Swagger Documentation
schema_view = get_swagger_view(title='API TextilesLolo - Documentacion General')

urlpatterns += [
    url(r'documentacion/', schema_view)
]