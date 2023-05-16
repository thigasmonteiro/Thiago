from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from garagem.views import (AcessorioViewSet, CategoriaViewSet, CorViewSet,
                           MarcaViewSet, VeiculoViewSet)

router = DefaultRouter()
router.register(r"acessorios", AcessorioViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cors", CorViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
