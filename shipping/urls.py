
from rest_framework.routers import DefaultRouter
from .api_views import ProductViewSet, BoxViewSet, OrderViewSet

router = DefaultRouter()

router.register("products", ProductViewSet, basename="product")
router.register("boxes", BoxViewSet, basename="box")
router.register("orders", OrderViewSet, basename="order")

urlpatterns = router.urls
