from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    filter_dropdown = (
        By.CLASS_NAME,
        "product_sort_container"
    )

    item_names = (By.CLASS_NAME,"inventory_item_name")

    item_prices = (By.CLASS_NAME,"inventory_item_price")

    # Actions
    def select_filter(self, value):

        dropdown = Select(
            self.driver.find_element(
                *self.filter_dropdown
            )
        )

        dropdown.select_by_value(value)

    def get_product_names(self):

        products = self.driver.find_elements(
            *self.item_names
        )

        return [p.text for p in products]

    def get_product_prices(self):

        prices = self.driver.find_elements(
            *self.item_prices
        )

        return [
            float(
                p.text.replace("$", "")
            )
            for p in prices
        ]