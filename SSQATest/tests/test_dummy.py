import pytest

@pytest.mark.usefixtures("init_driver")
class Test_dummy():

    def test_dummy_func(self):
        print("I AM DUMMY LINE 1")
        print("I AM DUMMY LINE 2")
        self.driver.get("https://supersqa.com/")
