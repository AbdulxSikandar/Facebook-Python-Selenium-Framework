import time


class Basedriver():

    def __init__(self, driver):
        self.driver = driver

    # def page_scroll(self):
    #     pageLength = self.driver.execute_script(
    #         "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight;")
    #     match = False
    #     while (match == False):
    #         lastCount == pageLength
    #         time.sleep(3)
    #         pageLength = self.driver.execute_script(
    #             "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight;")
    #         if lastCount == pageLength:
    #             match = True
    #         time.sleep(2)










