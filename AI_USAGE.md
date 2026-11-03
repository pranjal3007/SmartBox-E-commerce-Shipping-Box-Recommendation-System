# AI Usage Report – SmartBox E-commerce Shipping Box Recommendation System

## 1. AI Tools Used

**AI Tool:** ChatGPT (OpenAI)

I used ChatGPT as a development assistant while building the SmartBox E-commerce Shipping Box Recommendation System using Python, Django, and Django REST Framework.

I used AI assistance to understand unfamiliar concepts, troubleshoot errors, explore implementation approaches, write and debug test cases, and improve project documentation.

I did not rely on AI-generated code without checking it. I reviewed suggestions, adapted them to my project structure, and verified the results by running commands, testing API endpoints, and opening pages in the browser.

## 2. Actual Prompts and AI Assistance

The following are examples of prompts I actually used during the development conversations. They are grouped by development activity.

| Actual prompt / request | Purpose | How the assistance was used |
|---|---|---|
| "can we add other sample too" | Adding sample data to the project. | Discussed adding more sample records for testing. |
| "now i dont want the product_list page in json format and other too" | Improving the presentation of application data. | Explored separating frontend HTML pages from REST API responses. |
| "this is view.py" | Sharing the existing Django views implementation. | Used the existing code to integrate a visual Product List view without removing existing functionality. |
| "this is urls.py" | Sharing the application's URL configuration. | Reviewed API router configuration and added separate frontend routes. |
| "not displaying anythong" | Troubleshooting the Product List page. | Investigated URL routing, template rendering, and configuration. |
| "Same JSON/API page" | Reporting that the browser still displayed the API interface. | Checked the resolved Django view and tested the response using Django's test client. |
| Sharing the output of `resolve('/products/')` | Verifying which view handled the Product List URL. | Confirmed that Django resolved the URL to `product_list_page`. |
| Sharing the Django test client output showing `DisallowedHost` | Investigating a failed page test. | Identified that the test client was using `testserver` and reran the check using `localhost`. |

Other development conversations also involved requests for help understanding Django REST Framework, serializers, the packing algorithm, automated testing, and project documentation. The examples above are actual requests from the available conversation history, not a claim to be a complete export of every prompt used.

## 3. AI Suggestions: Accepted, Modified, and Rejected

### Accepted

- Guidance on organizing Django views and URL configurations.
- Explanations of Django REST Framework and serializer functionality.
- Suggestions for testing product rotation and multiple-product placement.
- Guidance on creating automated tests and investigating test failures.
- Suggestions for separating API endpoints from frontend pages.
- Guidance on documenting the project and preparing its submission.

### Modified and Verified

- AI-generated code was adapted to match the existing project structure rather than replacing the entire application.
- URL configuration suggestions were adjusted to preserve the existing homepage, recommendation page, admin panel, and API routes.
- Test expectations were checked against the actual API response structure.
- Template and frontend suggestions were incorporated while keeping the REST API available separately.
- The Product List page implementation was checked using Django's URL resolver and test client.

### Rejected or Corrected

Some AI guidance required correction or further investigation:

1. **Product List routing:** Initial troubleshooting focused on URL routing. However, the URL resolver later confirmed that `/products/` was correctly mapped to `product_list_page`. This showed that changing URL patterns repeatedly was not the right next step.

2. **Test client host:** The initial test command used Django's default `testserver` host and produced a `DisallowedHost` error. The test was rerun using `HTTP_HOST='localhost'` instead of unnecessarily changing the application's allowed hosts.

3. **Preserving API functionality:** The goal was to display normal HTML pages without losing the REST API. Suggestions that could unnecessarily replace or remove existing functionality were not appropriate for the project.

These examples show why I checked AI suggestions against actual application behaviour rather than accepting every suggestion directly.

## 4. Problems and Challenges Encountered

During development, I encountered the following problems:

1. **Django Admin:** I needed to create a superuser before accessing the Django Admin panel.

2. **Validation:** I faced issues while configuring validation rules for product and box data.

3. **PATCH Requests:** I tested updating individual product records using PATCH requests and checked whether the changes were reflected correctly.

4. **Serializers (`shipping/serializers.py`):** I encountered an import error because `serializers` was not defined. I investigated the import and checked the serializer configuration.

5. **Change in Development Approach:** Initially, I started developing the project using Django with HTML and CSS. Later, I switched to Django REST Framework to build REST APIs and manage application data through API endpoints.

6. **Packing Algorithm (`packing.py`):** I tested different packing scenarios, including product rotation, multiple products, unsuitable dimensions, and weight-limit conditions.

7. **Test Discovery:** Initially, Django reported `Found 0 test(s)` because test cases had not yet been added. I added automated test cases to `shipping/tests.py` and reran the test command.

8. **Test Failures:** Some tests initially failed because the recommendation returned a box object rather than a plain box-name string. I reviewed the response structure and corrected the test expectations.

9. **Django URL and Template Issues:** I encountered URL configuration problems and a missing recommendation template. I checked the URL patterns and template location and verified the pages after correcting the issues.

10. **Frontend and API Separation:** When I wanted the Product List page to display as a normal webpage instead of JSON, I needed to understand the difference between a REST API endpoint and a Django template-based view.

11. **URL Configuration During Frontend Integration:** I discovered that my main URL configuration contained two separate `urlpatterns` definitions. The second definition overwrote the first. I corrected the configuration so the homepage, admin panel, recommendation page, and API routes could work together.

12. **Django Test Client:** The test client initially returned a `DisallowedHost` error because it used `testserver`. I reran the check with `HTTP_HOST='localhost'` and received a successful HTML response.

## 5. Mistakes or Limitations in AI Assistance

AI assistance was useful, but not every suggestion was immediately correct or sufficient.

- Some initial frontend troubleshooting focused on URL routing before the actual HTML response had been verified.
- The initial test-client command did not account for the project's `ALLOWED_HOSTS` configuration.
- Some suggestions needed to be adapted to my existing files to avoid replacing working API or recommendation functionality.
- AI-generated code could not independently confirm that the page looked correct in my browser. I still needed to run the application and inspect the result.
- AI explanations and code suggestions were not treated as proof that the application worked.

I learned to provide the relevant source code and complete error output, test one change at a time, and verify the result before moving to the next task.

## 6. Verification and Testing

I verified the application through terminal commands, browser testing, and automated tests.

Commands used:

```bash
python manage.py check
python manage.py runserver
python manage.py shell
python manage.py test shipping -v 2
```

Additional debugging commands included:

```bash
python manage.py shell -c "from django.urls import resolve; print(resolve('/products/').func)"
```

```bash
python manage.py shell -c "from django.test import Client; r=Client(HTTP_HOST='localhost').get('/products/'); print('STATUS:', r.status_code); print(r.content[:1000].decode())"
```

Verification included:

- Checking Django system configuration.
- Running the development server and opening the homepage.
- Accessing REST API endpoints.
- Testing product creation and order operations.
- Testing PATCH requests.
- Testing the packing algorithm with sample products and boxes.
- Checking product rotation and multiple-product placement.
- Testing weight-limit and unsuitable-box scenarios.
- Checking the Django Admin panel.
- Checking the URL resolution for the Product List page.
- Verifying that the Product List view returned HTML with HTTP 200.
- Running automated tests.

**Final automated test status:** 19 tests passed in the latest recorded project verification. This count should match the final `python manage.py test shipping -v 2` output included in the submission.

## 7. My Responsibility

I was responsible for developing and verifying the SmartBox project.

My work included:

- Setting up the Django project and application.
- Implementing models and serializers.
- Developing REST API endpoints.
- Implementing the shipping box recommendation and packing logic.
- Configuring Django Admin.
- Writing and running automated tests.
- Debugging application errors.
- Testing API responses and application pages.
- Maintaining project documentation and the GitHub repository.

ChatGPT was used as a supporting tool to understand concepts, troubleshoot problems, and explore possible solutions. I reviewed, adapted, and verified the suggestions through actual application execution and testing.