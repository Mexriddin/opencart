import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeS
from selenium.webdriver.firefox.service import Service as firefoxS
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    """ Parameters passed to the command line when running test """
    parser.addoption("--url", action="store", default="https://demo-opencart.ru",  # "http://localhost:8080/opencart/"
                     help="This is base page_objects url")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, firefox, safari")
    parser.addoption("--wait", default=10,
                     help="This is time parameter for driver wait")
    parser.addoption("--implicitly_wait", default=3,
                     help="This is time parameter for driver implicitly wait")
    # parser.addoption("--log_file", default=None,
    #                  help="This is a file address, where selenium logs will be")
    # parser.addoption("--log_level", default="INFO",
    #                  help="This is a log level parameter")
    parser.addoption("--brversion", default="105", help="This is version remote browser")
    parser.addoption("--executor", default="local", help="Choose execute: local, remote")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--video", action="store_true", default=True)


def driver_factory(browser, brversion, executor, vnc, video, implicitly_wait):
    """ Preparing the driver with the given parameters """
    if executor == "local":
        if browser == "chrome":
            service = chromeS(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            # options.add_argument("headless")
            # options.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(options=options,
                                      service=service)
        elif browser == "firefox":
            service = firefoxS(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            # options.add_argument("-headless")
            # options.add_argument("--window-size=1920x1080")
            driver = webdriver.Firefox(options=options, service=service)
        elif browser == "safari":
            driver = webdriver.Safari()
        else:
            raise Exception("Browser not supported")
    elif executor == "remote":
        executor_url = f"https://{executor}:4444/wd/hub"
        caps = {
            "browserName": browser,
            "browserVersion": brversion,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": video
            }
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
    driver.maximize_window()
    driver.implicitly_wait(implicitly_wait)

    return driver


@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("--browser")
    brversion = request.config.getoption("--brversion")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")
    implicitly_wait = request.config.getoption("--implicitly_wait")

    driver = driver_factory(browser=browser, brversion=brversion,
                            executor=executor, vnc=vnc, video=video,
                            implicitly_wait=implicitly_wait)

    driver.t = request.config.getoption("--wait")
    driver.base_url = request.config.getoption("--url")

    allure.attach(
        name="capabilities",
        body=str(driver.capabilities),
        attachment_type=allure.attachment_type.TEXT
    )
    yield driver
    driver.quit()


# @pytest.fixture(scope="function")
# def wait(browser, request):
#     wait = request.config.getoption("--wait")
#     return WebDriverWait(browser, wait)


# @pytest.fixture(scope="function")
# def url(request):
#     url = request.config.getoption("--url")
#     return url
