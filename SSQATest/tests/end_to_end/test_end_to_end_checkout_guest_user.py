import pytest
from SSQATest.src.pages.HomePage import HomePage
from SSQATest.src.pages.Header import Header
from SSQATest.src.pages.CartPage import CartPage
from SSQATest.src.pages.CheckoutPage import Checkout
from SSQATest.src.pages.OrderRecievedPage import OrderRecievedPage
from SSQATest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser():

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        home_pg = HomePage(self.driver)
        header = Header(self.driver)
        cart_pg = CartPage(self.driver)
        checkout_pg = Checkout(self.driver)
        order_received_pg = OrderRecievedPage(self.driver)

    #         go to home page
        home_pg.go_to_home_page()
    #          add 1 item to cart
        home_pg.add_item_to_cart()
    #          make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1)
    #          go to cart
        header.click_on_cart_on_right_header()
        product_names = cart_pg.get_all_product_names_in_cart()
        assert len(product_names) == 1 , f"Expected 1 item in Cart but found {len(product_names)}"
    #          apply free coupon(ssqa100)
        coupon_code = GenericConfigs.FREE_COUPON
        cart_pg.apply_coupon(coupon_code)
    # click on checkout
        cart_pg.click_on_checkout_button()
    #           apply free shiping
    #           fill details & click on checkout
        checkout_pg.fill_in_billing_info()
        checkout_pg.click_place_order_btn()
    #           verify order is recieved
        order_received_pg.verify_order_recieved_page_loaded()
    #           verify order is recorded in DB(via SQL or API)
        order_no = order_received_pg.get_order_number()
        print("********")
        print(order_no)
        print("********")