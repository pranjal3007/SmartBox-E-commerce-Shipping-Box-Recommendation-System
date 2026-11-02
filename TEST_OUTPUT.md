"# SmartBox - Test Execution Results" | Set-Content TEST_OUTPUT.md

"`n## Django System Check" | Add-Content TEST_OUTPUT.md
python manage.py check 2>&1 | Tee-Object -FilePath TEST_OUTPUT.md -Append

"`n## Automated Test Suite" | Add-Content TEST_OUTPUT.md
python manage.py test shipping -v 2 2>&1 | Tee-Object -FilePath TEST_OUTPUT.md -Append