import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
import os

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        # Create folder if not exists
        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = (
            f"screenshots/{item.name}.png"
        )

        driver.save_screenshot(screenshot_path)

        with open(screenshot_path, "rb") as file:
            allure.attach(
                file.read(),
                name=item.name,
                attachment_type=allure.attachment_type.PNG
            )

            
@pytest.fixture
def driver():

    chrome_options = webdriver.ChromeOptions()

    # Use dedicated Selenium profile
    chrome_options.add_argument(
        r"--user-data-dir=C:\SeleniumProfile"
    )

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }


    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )

    driver.maximize_window()

    yield driver
    driver.quit()