from pages.cart import CartPage
from pages.login import LoginPage
from pages.checkout import Checkout
import time
import allure


@allure.title("Verify valid login")
def login(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")


@allure.title("Verify successful checkout process")
def test_checkout_success(driver):

    login(driver)

    cart = CartPage(driver)
    checkout = Checkout(driver)

    # Add product
    with allure.step("Product added to the cart"):
      cart.add_to_cart()

    # Open cart
    with allure.step("Checking the cart"):
      cart.open_cart()

    # Checkout click
    with allure.step("Clicking the checkout option"):
      checkout.click_checkout()
      time.sleep(2)

    # Add details
    with allure.step("Adding the details in checkout screen"):
      checkout.add_details("Bharathi","D","600001")
      time.sleep(2)

      assert "checkout-step-two" in driver.current_url


@allure.title("Verify order placed successfully")
def test_order_placement(driver):
    login(driver)

    cart = CartPage(driver)
    checkout = Checkout(driver)

    # Add product
    with allure.step("Product added to the cart"):
      cart.add_to_cart()

    # Open cart
    with allure.step("Checking the cart"):
      cart.open_cart()

    # Checkout click
    with allure.step("Clicking the checkout option"):
      checkout.click_checkout()

    # Add details
    with allure.step("Adding the details in checkout screen"):
      checkout.add_details("Bharathi","D","600001")

    with allure.step("Scrolling to the bottom"):
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
      time.sleep(3)
    
    # Checkout complete
    with allure.step("Thank you for your order!"):
      checkout.click_finish()
      assert "Thank you for your order!" in driver.page_source
    

@allure.title("Verify checkout validation for empty details")
def test_checkout_missing_fields(driver):

    login(driver)

    cart = CartPage(driver)
    checkout = Checkout(driver)

    with allure.step("Product added to the cart"):
      cart.add_to_cart()

    with allure.step("Checking the cart"):
      cart.open_cart()

    with allure.step("Clicking the checkout option"):
      checkout.click_checkout()

    with allure.step("Validating the missing details error case in checkout screen"):
      checkout.checkout_missing_fields()
      time.sleep(2)

      assert "Error" in checkout.get_error_message()