from django.contrib import admin
from django.urls import include, path

from shipping import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("shipping.urls")),
    path("", views.home, name="home"),
    path("recommendation/", views.recommendation_lookup, name="recommendation-lookup"),
    path(
        "orders/<int:order_id>/recommendation/",
        views.order_recommendation,
        name="order-recommendation",
    ),
]
