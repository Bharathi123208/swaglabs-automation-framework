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


