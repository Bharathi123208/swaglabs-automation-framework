from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    
    # Locator
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_msg = (By.CLASS_NAME, "error-message-container")
    
    
    # Actions
    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()

    def get_error(self):
        return self.driver.find_element(*self.error_msg).text