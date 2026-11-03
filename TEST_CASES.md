# SmartBox – Test Cases

## Objective

This document describes the automated test scenarios implemented in `shipping/tests.py`. The expected outcomes below are based on the assertions in those tests. Run the commands at the end to verify the current checkout; see `TEST_OUTPUT.md` for the recorded terminal output.

## Automated test cases

| Test ID | Test method | Scenario | Expected result |
|---|---|---|---|
| TC01 | `test_product_rotation` | A product needs a different orientation to fit in the box. | Packing succeeds with a rotated orientation. |
| TC02 | `test_multiple_products` | Multiple products are placed in one box. | A placement is returned for each product. |
| TC03 | `test_product_too_large` | A product is too large to fit in the box. | Packing returns no placement. |
| TC04 | `test_cheapest_suitable_box` | More than one suitable box is available at different costs. | The cheapest suitable box is selected. |
| TC05 | `test_weight_limit` | Order weight exceeds the box weight capacity. | Recommendation reports failure. |
| TC06 | `test_smaller_volume_tie_breaker` | Suitable boxes have the same cost. | The smaller-volume box is selected. |
| TC07 | `test_empty_order` | Recommendation is requested for an empty order. | Recommendation fails with the empty-order message. |
| TC08 | `test_placements_are_inside_box_and_do_not_overlap` | Validate product placement coordinates. | Placements stay within box boundaries and products do not overlap. |
| TC09 | `test_recommendation_api_success` | Request a recommendation for a valid order. | API returns HTTP 200 and a successful result. |
| TC10 | `test_recommendation_api_weight_failure` | Request a recommendation when the order exceeds weight capacity. | API returns HTTP 200 and a failure result. |
| TC11 | `test_recommendation_api_empty_order` | Request a recommendation for an order with no items. | API returns HTTP 200 and a failure result. |
| TC12 | `test_product_zero_dimension_rejected` | Submit a product with a zero dimension. | API returns HTTP 400. |
| TC13 | `test_product_negative_weight_rejected` | Submit a product with negative weight. | API returns HTTP 400. |
| TC14 | `test_box_negative_cost_rejected` | Submit a box with negative cost. | API returns HTTP 400. |
| TC15 | `test_order_zero_quantity_rejected` | Submit an order item with quantity zero. | API returns HTTP 400. |
| TC16 | `test_order_invalid_product_id_rejected` | Submit an order item with an invalid product ID. | API returns HTTP 400. |
| TC17 | `test_duplicate_products_rejected` | Submit duplicate product entries in one order. | API returns HTTP 400. |
| TC18 | `test_recommendation_page_loads_successfully` | Open the recommendation page for a valid order. | Page returns HTTP 200 and expected recommendation content. |
| TC19 | `test_recommendation_page_returns_404_for_invalid_order` | Open the recommendation page for an unknown order. | Page returns HTTP 404. |

## Run the tests

From the directory containing `manage.py`, activate your virtual environment and run:

```bash
python manage.py check
python manage.py test shipping -v 2
```

Update `TEST_OUTPUT.md` with the real output from your own run. Do not report tests as passing unless the commands finish successfully.
