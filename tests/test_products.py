from pages.login import LoginPage
from pages.product import ProductPage
from pages.checkout import Checkout
from pages.cart import CartPage
from selenium.webdriver.common.by import By
import time
import allure


def login(driver):

    login_page = LoginPage(driver)

    login_page.load()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

@allure.title("Verify products are sorted from accordingly")
def test_all_filters(driver):

    login(driver)

    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = Checkout(driver)

    filters = {
        "az": "A to Z",
        "za": "Z to A",
        "lohi": "Low to High",
        "hilo": "High to Low"
    }
    
    with allure.step("Checking the filters are selecting correctly based on options"):
     for value, name in filters.items():

        # Apply filter
        product.select_filter(value)

        time.sleep(2)

        # Validate sorting
        if value == "az":

            names = product.get_product_names()

            assert names == sorted(names), \
                f"{name} sorting failed"

        elif value == "za":

            names = product.get_product_names()

            assert names == sorted(
                names,
                reverse=True
            ), f"{name} sorting failed"

        elif value == "lohi":

            prices = product.get_product_prices()

            assert prices == sorted(prices), \
                f"{name} sorting failed"

        elif value == "hilo":

            prices = product.get_product_prices()

            assert prices == sorted(
                prices,
                reverse=True
            ), f"{name} sorting failed"

        # Add order
        cart.add_to_cart()

        cart.open_cart()

        checkout.click_checkout()

        checkout.add_details(
            "Bharathi",
            "D",
            "600001"
        )

        time.sleep(2)

        # Finish order
        driver.find_element(By.ID,"finish").click()

        # Validate order
        assert (
            "Thank you for your order!"
            in driver.page_source
        )

        print(f"{name} filter order passed")

        # Return to products page
        driver.find_element(
            By.ID,
            "back-to-products"
        ).click()