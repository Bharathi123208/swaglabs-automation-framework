from pages.login import LoginPage
import time
import allure



@allure.title("Verify valid login")
def test_valid_login(driver):
    
    login_page = LoginPage(driver)

    with allure.step("Open application"):
      login_page.load()

    with allure.step("Login with credentials"):
      login_page.login("standard_user", "secret_sauce") 
    time.sleep(2)
    
    with allure.step("Validate successful login"):
      assert "inventory" in driver.current_url
      assert "Swag Labs" in driver.title
   
@allure.title("Verify Invalid login")
def test_invalid_login(driver): 
    
    
    login = LoginPage(driver) 

    with allure.step("Open application"):
      login.load() 

    with allure.step("Login with invalid credentials"):
      login.login("wrong_user", "wrong_pass") 
    time.sleep(2)

    with allure.step("Validate unsuccessful login"):
      assert "Username and password do not match" in login.get_error()


@allure.title("Verify Locked User Validation")
def test_locked_user_login(driver):

    login = LoginPage(driver) 

    with allure.step("Open application"):
      login.load() 

    with allure.step("Login with locker user credentials"):
      login.login("locked_out_user", "secret_sauce")
    time.sleep(2)


    with allure.step("Verify locked user validation"):
      assert " Sorry, this user has been locked out" in login.get_error()

