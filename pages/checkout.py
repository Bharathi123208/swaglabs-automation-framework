from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    firstname = (By.ID, "first-name")
    lastname = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    checkout_btn = (By.ID, "checkout")
    error_msg = (By.CLASS_NAME, "error-message-container")
    finish = (By.XPATH, "//button[@id='finish']")

    # Actions
    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()
    
    def click_finish(self):
        self.driver.find_element(*self.finish).click()

    def add_details(self, f_name, l_name, ps_code):
        self.driver.find_element(*self.firstname).send_keys(f_name)
        self.driver.find_element(*self.lastname).send_keys(l_name)
        self.driver.find_element(*self.postal_code).send_keys(ps_code)
        self.driver.find_element(*self.continue_btn).click()

    def checkout_missing_fields(self):
        self.driver.find_element(*self.continue_btn).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
    
    


    