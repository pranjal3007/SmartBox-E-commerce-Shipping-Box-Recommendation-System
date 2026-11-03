# SmartBox – Test Execution Output

## 1. Test Environment

- Framework: Django
- Application: `shipping`
- Test runner: Django test framework
- Environment: Python virtual environment (`.venv`)
- Database: In-memory test database

## 2. Command Executed

```bash
python manage.py test shipping -v 2
```

## 3. Test Results

- Total tests found: **19**
- Tests passed: **19**
- Tests failed: **0**
- Errors: **0**
- Final result: **OK**

## 4. Actual Terminal Output

```text
Found 19 test(s).
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, rest_framework, staticfiles
  Apply all migrations: admin, auth, contenttypes, sessions, shipping
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0003_alter_email_validators... OK
  Applying auth.0004_alter_user_email_validators... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_opts_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying shipping.0001_initial... OK
  Applying shipping.0002_alter_product_height_alter_product_length_and_more... OK
  Applying shipping.0003_alter_box_internal_height_alter_box_internal_length_and_more... OK
System check identified no issues (0 silenced).

test_box_negative_cost_rejected (shipping.tests.APIValidationTests.test_box_negative_cost_rejected) ... ok
test_duplicate_products_rejected (shipping.tests.APIValidationTests.test_duplicate_products_rejected) ... ok
test_order_invalid_product_id_rejected (shipping.tests.APIValidationTests.test_order_invalid_product_id_rejected) ... ok
test_order_zero_quantity_rejected (shipping.tests.APIValidationTests.test_order_zero_quantity_rejected) ... ok
test_product_negative_weight_rejected (shipping.tests.APIValidationTests.test_product_negative_weight_rejected) ... ok
test_product_zero_dimension_rejected (shipping.tests.APIValidationTests.test_product_zero_dimension_rejected) ... ok
test_cheapest_suitable_box (shipping.tests.PackingAlgorithmTests.test_cheapest_suitable_box) ... ok
test_empty_order (shipping.tests.PackingAlgorithmTests.test_empty_order) ... ok
test_multiple_products (shipping.tests.PackingAlgorithmTests.test_multiple_products) ... ok
test_placements_are_inside_box_and_do_not_overlap (shipping.tests.PackingAlgorithmTests.test_placements_are_inside_box_and_do_not_overlap) ... ok
test_product_rotation (shipping.tests.PackingAlgorithmTests.test_product_rotation) ... ok
test_product_too_large (shipping.tests.PackingAlgorithmTests.test_product_too_large) ... ok
test_smaller_volume_tie_breaker (shipping.tests.PackingAlgorithmTests.test_smaller_volume_tie_breaker) ... ok
test_weight_limit (shipping.tests.PackingAlgorithmTests.test_weight_limit) ... ok
test_recommendation_api_empty_order (shipping.tests.RecommendationAPITests.test_recommendation_api_empty_order) ... ok
test_recommendation_api_success (shipping.tests.RecommendationAPITests.test_recommendation_api_success) ... ok
test_recommendation_api_weight_failure (shipping.tests.RecommendationAPITests.test_recommendation_api_weight_failure) ... ok
test_recommendation_page_loads_successfully (shipping.tests.VisualRecommendationPageTests.test_recommendation_page_loads_successfully) ... ok
test_recommendation_page_returns_404_for_invalid_order (shipping.tests.VisualRecommendationPageTests.test_recommendation_page_returns_404_for_invalid_order) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.084s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
```

## 5. Conclusion

All 19 automated tests completed successfully.

The tests covered API input validation, packing algorithm behaviour, box recommendation, weight restrictions, product rotation, and recommendation page responses.

The Django test runner reported no system-check issues during execution.