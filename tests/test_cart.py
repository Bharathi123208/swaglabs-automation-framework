from pages.cart import CartPage
from pages.login import LoginPage
import time
import allure

@allure.title("Verify valid login")
def login(driver):
    login_page = LoginPage(driver)

    with allure.step("Open application"):
      login_page.load()

    with allure.step("Login with credentials"):
      login_page.login("standard_user", "secret_sauce")


@allure.title("Verify product can be added to cart")
def test_add_to_cart(driver):

    login(driver)

    cart = CartPage(driver)

    with allure.step("Product added to the cart"):
      cart.add_to_cart()
      time.sleep(2)

    with allure.step("Cart items count"):
      assert cart.get_cart_count() == "2"
    

@allure.title("Verify product can be removed from cart")
def test_remove_from_cart(driver):

    login(driver)

    cart = CartPage(driver)

    with allure.step("Product added to the cart"):
      cart.add_to_cart()

    with allure.step("Product removed from the cart"):
      cart.remove_from_cart()
      time.sleep(2)

    badge = driver.find_elements(*cart.cart_badge)

    with allure.step("Cart items count after removal"):
       
      assert len(badge) == 1