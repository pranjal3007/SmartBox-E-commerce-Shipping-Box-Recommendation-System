
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Product, Box, Order
from .serializers import (
    ProductSerializer,
    BoxSerializer,
    OrderSerializer
)
from .packing import recommend_box


class ProductViewSet(viewsets.ModelViewSet):
    """
    API for managing e-commerce products.

    Supports creating, retrieving, updating and deleting products.
    Each product contains its name, dimensions and weight.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class BoxViewSet(viewsets.ModelViewSet):
    """
    API for managing available shipping boxes.

    Supports creating, retrieving, updating and deleting boxes.
    Each box has internal dimensions, maximum weight capacity and cost.
    """
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [AllowAny]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API for managing customer shipping orders.

    Supports creating, retrieving, updating and deleting orders.
    Also provides an endpoint to recommend a suitable shipping box
    based on product dimensions, weight and box cost.
    """
    queryset = Order.objects.prefetch_related(
        'items__product'
    ).all()

    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

   
    @action(
        detail=True,
        methods=["get"],
        url_path="recommend-box"
    )
    def recommend_box_for_order(self, request, pk=None):
        """
        Recommend the cheapest suitable shipping box for an order.

        Checks box weight capacity and attempts 3D product packing.
        Product rotation is allowed. Returns product placements
        and rejected box reasons.
        """

        # Retrieve the requested order.
        order = self.get_object()


        # Get products and quantities from the order.
        order_products = []

        for order_item in order.items.select_related("product"):
            product = order_item.product

            order_products.append({
                "name": product.name,
                "length": float(product.length),
                "width": float(product.width),
                "height": float(product.height),
                "weight": float(product.weight),
                "quantity": order_item.quantity
            })

        # Get available shipping boxes.
        available_boxes = []

        for box in Box.objects.all():
            available_boxes.append({
                "name": box.name,
                "length": float(box.internal_length),
                "width": float(box.internal_width),
                "height": float(box.internal_height),
                "max_weight": float(box.max_weight),
                "cost": float(box.cost)
            })

        # Generate recommendation.
        result = recommend_box(
            order_products,
            available_boxes
        )

        return Response(result)
