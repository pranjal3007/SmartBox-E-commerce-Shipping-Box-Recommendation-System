
from django.contrib import admin
from django.urls import path, include
from shipping.views import home, order_recommendation, recommendation_lookup

urlpatterns = [
    path("", home, name="home"),
    path(
        "recommendation/",
        recommendation_lookup,
        name="recommendation-lookup"
    ),
    path(
        "orders/<int:order_id>/recommendation/",
        order_recommendation,
        name="order-recommendation"
    ),
    path("admin/", admin.site.urls),
    path("api/", include("shipping.urls")),
]
