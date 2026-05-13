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

## Framework Features

- Page Object Model (POM) architecture
- Reusable page methods
- End-to-end automation flow
- Detailed Allure reporting
- Pass/Fail execution summary
- Scalable test structure
- Screenshot capture for failed tests

## Future Enhancements

- Jenkins CI/CD Integration
- Parallel Test Execution
- Cross Browser Testing
- Data-Driven Testing
  
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
```
## Framework Demo

Click below to watch automation execution video

![Framework Walkthrough] https://github.com/Bharathi123208/swaglabs-automation-framework/issues/1#issue-4439558356


# Snapshots of Allure Report and Dashboard

## Allure Report

![Allure Report](assets/Reports.png)


## Suite Report
![Suite Report](assets/Suites.png)


## Test Execution Report

![Test Report](assets/Dashboard.png)


## Category Tab

![Category1 Report](assets/category_1.png)

![Category2 Report](assets/category_2.png)

## Timeline Tab

![Timeline Report](assets/Timeline.png)

## Packages and Behaviour Tab

![Packages Report](assets/Behaviour.png)

![Behaviour Report](assets/Packages.png)


## Installation

### Clone Repository

```bash
git clone <your-github-repository-link>
```

### Navigate to Project Folder

```bash
cd Auto_Sauce
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running Test Cases

### Run Complete Test Suite

```bash
python -m pytest -v --alluredir=reports
```

### Run Specific Test File

```bash
python -m pytest tests/test_login.py
```

## Generate Allure Report

### Generate Report

```bash
allure generate reports -o allure-report --clean
```

### Open Report

```bash
allure serve reports
```

## Author

**Bharathi D**  
SDET | Automation Testing | Selenium | Python | API Testing



