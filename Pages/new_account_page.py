from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from Project1.Base.base_class import Basedriver
from Project1.Utilities.utils import Utils


class Newaccount(Basedriver):

    # log = Utils.getLogger()

    def __init__(self, driver):
        super().__init__(driver)     # This is Basedriver constructor to inherit the methods of Parent class in child
        self.driver = driver

    def acc_page(self):
        nextpage = self.driver.find_element(By.XPATH,"//a[@data-testid= 'open-registration-form-button']")
        nextpage.click()

    FName_Field = "firstname"
    LName_Field = "lastname"
    Mail_Field = "reg_email__"
    RMail_Field = "reg_email_confirmation__"
    NEWPASS_Field = "reg_passwd__"
    BDAY_Field = "day"
    BMON_Field = "month"
    BYEAR_Field = "year"
    SEX_Field = "//label[text()='Male']"
    SIGNUP_Field = "websubmit"

    def fname(self, fname):
        firstname = self.driver.find_element(By.NAME, self.FName_Field)
        firstname.send_keys(fname)

    def lname(self, lname):
        lastname = self.driver.find_element(By.NAME, self.LName_Field)
        lastname.send_keys(lname)

    def newmail(self, newmail):
        regmail = self.driver.find_element(By.NAME, self.Mail_Field)
        regmail.send_keys(newmail)
        time.sleep(2)

    def remail(self, samemail):
        remail = self.driver.find_element(By.NAME, self.RMail_Field)
        remail.send_keys(samemail)
        time.sleep(2)

    def newpasswd(self, newpass):
        newpasswd = self.driver.find_element(By.NAME, self.NEWPASS_Field)
        newpasswd.send_keys(newpass)

    def bday(self, day):
        bday = Select(self.driver.find_element(By.ID, self.BDAY_Field))
        bday.select_by_visible_text(day)

    def bmonth(self, month):
        bmonth = Select(self.driver.find_element(By.ID, self.BMON_Field))
        bmonth.select_by_visible_text(month)

        # op = mon.options
        # for option in op:
        #     print(option.text)
        # print(f"Count of all the given options: {len(mon.options)}")

    def byear(self, year):
        byear = Select(self.driver.find_element(By.ID, self.BYEAR_Field))
        byear.select_by_visible_text(year)

        # find out all the links available in the page
        # links = driver.find_element((By.TAG_NAME,"a"))

        # to Print all the lin available on that page
        # for link in links:
        #   print(link.text)

        # to click on a particuler link of the page
        # select contact link and click on that button or link
        # driver.find_element(By.LINK_TEXT,"Contact").click()

        # Radio button selection
        # Sex Selection button

    def sex(self, mfsex):
        # mfsex = Male or Female or Custom
        sex = self.driver.find_element(By.XPATH, self.SEX_Field)
        sex.click()

        # sex = driver.find_element(By.XPATH,"//label[text()='Custom']")
        # print(sex.is_selected())
        # sex.click()
        time.sleep(3)

    def signup(self):
        # Sign up Button
        signup = self.driver.find_element(By.NAME, self.SIGNUP_Field)
        signup.click()

    def newaccount(self, fname, lname, newmail, samemail, newpass, day, month, year, mfsex):
        self.fname(fname)
        self.lname(lname)
        self.newmail(newmail)
        self.remail(samemail)
        self.newpasswd(newpass)
        self.bday(day)
        self.bmonth(month)
        self.byear(year)
        self.sex(mfsex)
        self.signup()