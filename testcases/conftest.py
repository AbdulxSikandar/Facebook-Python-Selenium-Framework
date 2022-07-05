import pytest
from selenium import webdriver
driver = None


@pytest.fixture(autouse=True)
def driver_setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

# ---------------------------------------------------------------------------------


# ----- Need to Fix This ------


# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType
# from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
# from webdriver_manager.opera import OperaDriverManager


# @pytest.fixture(autouse=True)
# def driver_setup(request, browser_name, url):
#     global driver
#     if browser_name == "chrome":
#         driver = webdriver.Chrome()
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox()
    # elif browser_name == "Edge":
    #     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    # elif browser_name == "IE":
    #     driver = webdriver.Ie(IEDriverManager().install())
    # elif browser_name == "Opera":
    #     driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    # elif browser_name == "Chromium":
    #     driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    # elif browser_name == "BRAVE":
    #     driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
    # else:
    #     driver = webdriver.Chrome()
    # driver.get(url)
    # driver.maximize_window()
    # request.cls.driver = driver
    # driver.implicitly_wait(2)
    # yield
    # driver.close()
    #
    # def pytest_addoption(parser):
    #     parser.addoption("--browser_name")

    # def pytest_addoption(parser):
    #     parser.addoption("--url")

    # @pytest.fixture(scope="class", autouse=True)
    # def browser(request):
    #      return request.config.getoption("--browser_name")

    # @pytest.fixture(scope="class", autouse=True)
    # def browser(request):
    #      return request.config.getoption("--url")
