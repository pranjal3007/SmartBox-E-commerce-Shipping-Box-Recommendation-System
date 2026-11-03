
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Product, Box, Order, OrderItem

from .packing import (
    pack_products,
    recommend_box,
    check_overlap
)

class PackingAlgorithmTests(TestCase):

    def test_product_rotation(self):
        products = [{
            "name": "Product A",
            "length": 20,
            "width": 10,
            "height": 5
        }]

        box = {
            "length": 5,
            "width": 20,
            "height": 10
        }

        result = pack_products(products, box)

        self.assertIsNotNone(result)
        self.assertEqual(result[0]["dimensions"], (5, 20, 10))

    def test_multiple_products(self):
        products = [
            {"name": "Laptop", "length": 30, "width": 20, "height": 5},
            {"name": "Mouse", "length": 10, "width": 6, "height": 4}
        ]

        box = {"length": 45, "width": 30, "height": 15}

        result = pack_products(products, box)

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

    def test_product_too_large(self):
        products = [{
            "name": "Large",
            "length": 100,
            "width": 100,
            "height": 100
        }]

        box = {"length": 10, "width": 10, "height": 10}

        self.assertIsNone(pack_products(products, box))

    def test_cheapest_suitable_box(self):
        order = [{
            "name": "Laptop",
            "length": 30,
            "width": 20,
            "height": 5,
            "weight": 2,
            "quantity": 1
        }]

        boxes = [
            {
                "name": "Medium",
                "length": 45,
                "width": 30,
                "height": 15,
                "max_weight": 5,
                "cost": 20
            },
            {
                "name": "Large",
                "length": 60,
                "width": 45,
                "height": 30,
                "max_weight": 15,
                "cost": 40
            }
        ]

        result = recommend_box(order, boxes)

        self.assertTrue(result["success"])
        self.assertEqual(
            result["recommended_box"]["name"],
            "Medium"
        )

    def test_weight_limit(self):
        order = [{
            "name": "Heavy Product",
            "length": 10,
            "width": 10,
            "height": 10,
            "weight": 20,
            "quantity": 1
        }]

        boxes = [{
            "name": "Small",
            "length": 20,
            "width": 20,
            "height": 20,
            "max_weight": 5,
            "cost": 10
        }]

        result = recommend_box(order, boxes)

        self.assertFalse(result["success"])

    def test_smaller_volume_tie_breaker(self):
        order = [{
            "name": "Product",
            "length": 10,
            "width": 10,
            "height": 5,
            "weight": 1,
            "quantity": 1
        }]

        boxes = [
            {
                "name": "Large Box",
                "length": 40,
                "width": 30,
                "height": 20,
                "max_weight": 10,
                "cost": 20
            },
            {
                "name": "Compact Box",
                "length": 25,
                "width": 20,
                "height": 15,
                "max_weight": 10,
                "cost": 20
            }
        ]

        result = recommend_box(order, boxes)

        self.assertEqual(
            result["recommended_box"]["name"],
            "Compact Box"
        )

    def test_empty_order(self):
        result = recommend_box([], [])

        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Order contains no products.")

    
    def test_placements_are_inside_box_and_do_not_overlap(self):

        products = [
            {
                "name": "Laptop",
                "length": 30,
                "width": 20,
                "height": 5
            },
            {
                "name": "Keyboard",
                "length": 40,
                "width": 15,
                "height": 3
            },
            {
                "name": "Mouse",
                "length": 10,
                "width": 6,
                "height": 4
            },
            {
                "name": "Mouse",
                "length": 10,
                "width": 6,
                "height": 4
            }
        ]

        box = {
            "length": 45,
            "width": 30,
            "height": 15
        }

        placements = pack_products(products, box)

        self.assertIsNotNone(placements)
        self.assertEqual(len(placements), 4)

        # Check every product stays inside the box.
        for item in placements:
            x, y, z = item["position"]
            length, width, height = item["dimensions"]

            self.assertGreaterEqual(x, 0)
            self.assertGreaterEqual(y, 0)
            self.assertGreaterEqual(z, 0)

            self.assertLessEqual(x + length, box["length"])
            self.assertLessEqual(y + width, box["width"])
            self.assertLessEqual(z + height, box["height"])

        # Check that no two products overlap.
        for i in range(len(placements)):
            for j in range(i + 1, len(placements)):

                self.assertFalse(
                    check_overlap(
                        placements[i]["position"],
                        placements[i]["dimensions"],
                        placements[j]
                    )
                )


class RecommendationAPITests(APITestCase):

    def setUp(self):
        self.laptop = Product.objects.create(
            name="Test Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        Box.objects.create(
            name="Test Small",
            internal_length=15,
            internal_width=10,
            internal_height=10,
            max_weight=1,
            cost=10
        )

        Box.objects.create(
            name="Test Medium",
            internal_length=45,
            internal_width=30,
            internal_height=15,
            max_weight=5,
            cost=20
        )

        self.order = Order.objects.create(
            order_number="TEST-ORDER-001"
        )

        OrderItem.objects.create(
            order=self.order,
            product=self.laptop,
            quantity=1
        )

        self.url = f"/api/orders/{self.order.id}/recommend-box/"

    def test_recommendation_api_success(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["success"])
        self.assertEqual(
            response.data["recommended_box"]["name"],
            "Test Medium"
        )

    def test_recommendation_api_weight_failure(self):
        self.laptop.weight = 20
        self.laptop.save()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data["success"])

    def test_recommendation_api_empty_order(self):
        empty_order = Order.objects.create(
            order_number="TEST-ORDER-EMPTY"
        )

        response = self.client.get(
            f"/api/orders/{empty_order.id}/recommend-box/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data["success"])

class APIValidationTests(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Validation Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

    def test_product_zero_dimension_rejected(self):
        response = self.client.post(
            "/api/products/",
            {
                "name": "Invalid Product",
                "length": 0,
                "width": 10,
                "height": 5,
                "weight": 1
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_product_negative_weight_rejected(self):
        response = self.client.post(
            "/api/products/",
            {
                "name": "Invalid Product",
                "length": 10,
                "width": 10,
                "height": 10,
                "weight": -2
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_box_negative_cost_rejected(self):
        response = self.client.post(
            "/api/boxes/",
            {
                "name": "Invalid Box",
                "internal_length": 30,
                "internal_width": 20,
                "internal_height": 10,
                "max_weight": 5,
                "cost": -10
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_order_zero_quantity_rejected(self):
        response = self.client.post(
            "/api/orders/",
            {
                "order_number": "INVALID-QUANTITY",
                "items": [
                    {
                        "product": self.product.id,
                        "quantity": 0
                    }
                ]
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_order_invalid_product_id_rejected(self):
        response = self.client.post(
            "/api/orders/",
            {
                "order_number": "INVALID-PRODUCT",
                "items": [
                    {
                        "product": 999999,
                        "quantity": 1
                    }
                ]
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_duplicate_products_rejected(self):
        response = self.client.post(
            "/api/orders/",
            {
                "order_number": "DUPLICATE-PRODUCT",
                "items": [
                    {
                        "product": self.product.id,
                        "quantity": 1
                    },
                    {
                        "product": self.product.id,
                        "quantity": 2
                    }
                ]
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

class VisualRecommendationPageTests(TestCase):

    def setUp(self):
        # Create a test product.
        self.product = Product.objects.create(
            name="Test Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        # Create a suitable shipping box.
        Box.objects.create(
            name="Test Medium",
            internal_length=45,
            internal_width=30,
            internal_height=15,
            max_weight=5,
            cost=20
        )

        # Create an order.
        self.order = Order.objects.create(
            order_number="VISUAL-TEST-001"
        )

        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

    def test_recommendation_page_loads_successfully(self):
        url = reverse(
            "order-recommendation",
            kwargs={"order_id": self.order.id}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "shipping/recommendation.html"
        )
        self.assertContains(response, "Suitable shipping box found!")
        self.assertContains(response, "Test Medium")

    def test_recommendation_page_returns_404_for_invalid_order(self):
        url = reverse(
            "order-recommendation",
            kwargs={"order_id": 999999}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
