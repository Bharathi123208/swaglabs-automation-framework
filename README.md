# SwagLabs E-Commerce Automation Framework

A Selenium-based test automation framework developed for end-to-end testing of the SwagLabs E-Commerce web application using Python, Pytest, Page Object Model (POM), and Allure Reporting.

## Project Overview

This framework automates critical user workflows and validates core functionalities of the SwagLabs E-Commerce application.

### Covered Test Scenarios

- Valid Login
- Invalid Login
- Add Product to Cart
- Remove Product from Cart
- Product Sorting (Low to High / High to Low)
- Checkout Flow
- UI Validation
- Error Message Validation

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Allure Reporting
- WebDriver Manager

## Project Structure

```text
Auto_Swag_Lab/
│
├── pages/
│   ├── login.py
│   ├── cart.py
│   ├── checkout.py
│   └── products.py
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_products.py
│
├── screenshots/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


### Project Structure

#### Clone the repository

git clone <your-github-repo-link>

#### Navigate to project folder

cd Auto_Sauce

#### Install dependencies

pip install -r requirements.txt

#### Running Test Cases

### Run complete test suite:

python -m pytest -v --alluredir=reports

### Run a specific test file:

python -m pytest tests/test_login.py

## Generate Allure Report

### Generate report:

allure generate reports -o allure-report --clean

### Open report:

allure serve reports

Framework Features

Page Object Model (POM) architecture
Reusable page methods
End-to-end automation flow
Detailed Allure reporting
Pass/Fail execution summary
Scalable test structure
Screenshot capture for failed tests
Future Enhancements
Jenkins CI/CD Integration
Parallel Test Execution
Cross Browser Testing
Data-Driven Testing

# Author
Bharathi D
SDET | Automation Testing | Selenium | Python | API Testing