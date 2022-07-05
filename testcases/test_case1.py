import time
import pytest


from Project1.Pages.fb_login_page import Loginpage
from Project1.Pages.new_account_page import Newaccount
# from Project1.Utilities import utils
# from ddt import ddt, data, unpack


@pytest.mark.usefixtures("driver_setup")
# @ddt
class Test_facebook:

    # log = Utils.getLogger(self)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lgn = Loginpage(self.driver)
        self.acc = Newaccount(self.driver)

    def test_title(self):
        print(self.driver.title)
        # print(self.driver.current_url)
        # self.log.info(self.driver.title)
        print(self.driver.current_url)
        assert self.driver.title in 'Facebook – log in or sign up'

    # @data(*utils.Utils.read_data_from_excel(self))
    # @unpack
    def test_login(self):
        self.lgn.signin("Sikandar123@gmail.com", "RJ11dj@4848")

    def test_newacc(self):
        self.acc.acc_page()
        time.sleep(5)
        self.acc.newaccount("Sikandar", "Khan", "Sikandar123@gmail.com", "Sikandar123@gmail.com",
                            "RJ49ca@6495", "15", "Jan", "1996", "Male")
