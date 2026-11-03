
from django.shortcuts import render, get_object_or_404, redirect

from .models import Order, Box
from .packing import recommend_box


def home(request):
    return render(request, "shipping/home.html")


def order_recommendation(request, order_id):
    """
    Display a visual shipping box recommendation for an order.
    """

    order = get_object_or_404(Order, id=order_id)

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

    result = recommend_box(order_products, available_boxes)

    return render(
        request,
        "shipping/recommendation.html",
        {
            "order": order,
            "result": result
        }
    )

from django.shortcuts import redirect

def recommendation_lookup(request):
    """
    Find an order and redirect to its recommendation dashboard.
    """
    if request.method == "POST":
        order_id = request.POST.get("order_id", "").strip()

        if order_id.isdigit() and Order.objects.filter(id=int(order_id)).exists():
            return redirect(
                "order-recommendation",
                order_id=int(order_id)
            )

        return render(
            request,
            "shipping/home.html",
            {"lookup_error": "Please enter a valid existing Order ID."}
        )

    return redirect("home")
