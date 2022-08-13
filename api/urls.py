from rest_framework import routers

from . import views

app_name = "api"
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'sobreviventes', views.SobreviventeViewSet,
                basename='sobreviventes')
router.register(r'itens', views.ItensViewSet,
                basename='itens')
router.register(r'inventario', views.InventarioViewSet,
                basename='inventario')

router.register(r'sinalizar', views.SinalizarViewSet,
                basename='sinalizar')

router.register(r'negociar', views.NegociarViewSet,
                basename='negociar')


# router.register(r'itens', views.ClienteViewSet, basename='cliente')
# # router.register(r'sinalizar', views.PedidoViewSet, basename='pedido')
urlpatterns = []
urlpatterns += router.urls
