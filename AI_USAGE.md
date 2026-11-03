# AI Usage Report – SmartBox E-commerce Shipping Box Recommendation System

## 1. AI Tools Used

**AI Tool:** ChatGPT (OpenAI)

I used ChatGPT as a development assistant while building the SmartBox E-commerce Shipping Box Recommendation System using Python, Django, and Django REST Framework.

AI assistance was used for:

- Understanding Django project structure and Django REST Framework.
- Understanding REST API development and serializers.
- Troubleshooting Python import errors and Django configuration issues.
- Understanding and testing the 3D product-packing algorithm.
- Debugging automated test cases.
- Improving project documentation and understanding Git commands.

AI was used as a supporting tool. I reviewed suggestions and verified changes by running the application and tests.

## 2. Prompts and AI Assistance

The following are descriptions of the types of prompts used during development, not verbatim copies of every original prompt.

| Area | Prompt purpose | How the assistance was used |
|---|---|---|
| Django setup | Understand how to set up a Django project and organize its components. | Used as guidance for project structure and configuration. |
| REST API development | Understand how to create APIs using Django REST Framework. | Used while developing API endpoints and working with serializers. |
| Packing algorithm | Understand how to fit multiple products inside a shipping box, including rotation. | Used to understand product placement and box recommendation logic. |
| Debugging | Troubleshoot Python import errors, URL configuration, and template problems. | Used error messages to investigate and correct issues. |
| Testing | Understand how to write and run automated tests for the application. | Used while developing and debugging test cases. |
| Documentation | Organize README and AI usage documentation. | Used to improve documentation structure and clarity. |

## 3. AI Suggestions: Accepted, Modified, and Rejected

### Accepted
- Guidance for understanding Django and Django REST Framework.
- Explanations of serializers and REST API concepts.
- Suggestions for testing product rotation and multiple-product placement.
- Guidance for organizing automated tests.
- Documentation structure suggestions.

### Modified and Verified
- Debugging suggestions were checked against actual terminal error messages.
- Packing algorithm examples were tested using sample products and boxes.
- Test expectations were adjusted according to the actual API response structure.
- Changes to the project were tested before being retained.

### Rejected
I did not document any specific AI suggestion as rejected during development. I avoided applying suggestions that did not match the actual project requirements or code without further verification.

## 4. Problems and Challenges Encountered

During development, I encountered the following problems:

1. **Django Admin:** I needed to create a superuser before accessing the Django Admin panel.

2. **Validations:** I faced issues while configuring validation rules for product and box data.

3. **PATCH Requests:** I tested updating individual product records using PATCH requests and checked whether the changes were reflected correctly.

4. **Serializers (`shipping/serializers.py`):** I encountered an import error because `serializers` was not defined. I investigated the import and checked the serializer configuration.

5. **Change in Development Approach:** Initially, I started developing the project using Django with HTML and CSS. Later, I switched to Django REST Framework to build REST APIs and manage application data through API endpoints.

6. **Packing Algorithm (`packing.py`):** I tested different packing scenarios, including product rotation, multiple products, unsuitable dimensions, and weight-limit conditions.

7. **Test Discovery:** Initially, Django reported `Found 0 test(s)` because test cases had not yet been added. I added automated test cases to `shipping/tests.py` and reran the test command.

8. **Test Failures:** Some tests initially failed because the recommendation returned a box object rather than a plain box-name string. I reviewed the response structure and corrected the test expectations.

9. **Django URL and Template Issues:** I encountered URL configuration problems and a missing recommendation template. I checked the URL patterns and template location and verified the pages after correcting the issues.

## 5. Verification and Testing

I verified the application through terminal commands, browser testing, and automated tests.

Commands used:

```bash
python manage.py check
python manage.py runserver
python manage.py shell
python manage.py test shipping -v 2
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
- Running automated tests.

**Final test status:** 19 automated tests passed in the latest recorded project verification.

## 6. My Responsibility

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

ChatGPT was used as a supporting tool to understand concepts, troubleshoot problems, and explore possible solutions. I verified the implemented changes through actual application execution and testing.