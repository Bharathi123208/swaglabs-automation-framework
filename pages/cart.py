from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    filter = (By.CLASS_NAME, "product_sort_container")
    white_shirt = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']")

    # Actions
    def add_to_cart(self):
        self.driver.find_element(*self.backpack).click()
        self.driver.find_element(*self.white_shirt).click()


    def remove_from_cart(self):
        self.driver.find_element(*self.remove_backpack).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()