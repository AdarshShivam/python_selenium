import pytest
from SSQATest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from SSQATest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from SSQATest.src.helpers.generic_helpers import generate_random_email_and_password

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):

        my_account_out = MyAccountSignedOut(self.driver)
        my_account_in = MyAccountSignedIn(self.driver)

        # go to my account
        my_account_out.go_to_my_account()
        # Enter Email
        rand_email = generate_random_email_and_password()
        # print(rand_email["email"])
        my_account_out.input_register_email(email=rand_email)
        # Enter password
        my_account_out.input_register_password("adarsh@123")
        # click on register
        my_account_out.onclick_register_button()
        # verify user is registered
        my_account_in.onclick_logout_button()
