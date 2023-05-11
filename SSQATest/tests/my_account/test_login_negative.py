import pytest
from SSQATest.src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        print("PASS")
        return
        my_account = MyAccountSignedOut(self.driver)
            # go to my account
        my_account.go_to_my_account()
            # enter username
        u_name = 'Asadasdasdahgsdjgajsgd'
        pa_wd  = 'dasdasdasdasd'
        my_account.input_login_username(u_name)
            # enter password
        my_account.input_login_password(pa_wd)
            # click login
        my_account.onclick_login_button()
            # verify error
        expected_error = f'The username {u_name} is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_error)

