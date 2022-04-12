import pytest
import allure
from selenium import webdriver
from webdriver_manager import chrome, firefox
from framework import config
from allure_commons.types import AttachmentType

@pytest.fixture(scope="session")
def driver():
    driver = config.BROWSER
    if driver == "chrome":
        driver_path = chrome.ChromeDriverManager().install()
        driver = webdriver.Chrome(executable_path=driver_path)
    elif driver == "firefox":
        driver_path = firefox.GeckoDriverManager().install()
        driver = webdriver.Firefox(executable_path=driver_path)
    else:
        raise RuntimeError(f'Browser {driver} was not supported. Supported browsers: {config.SUPPORTED_BROWSERS}')
    driver.delete_all_cookies()
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def attaching_screenshot_on_fail(request, driver):
    yield
    if request.node.rep_setup.failed:
        print("Test set up failed!", request.node.nodeid)
        allure.attach(driver.get_screenshot_as_png(), name='SetUpScreenshot', attachment_type=AttachmentType.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            print("Test execution has failed", request.node.nodeid)
            allure.attach(driver.get_screenshot_as_png(), name='CallScreenshot', attachment_type=AttachmentType.PNG)
    elif request.node.rep_teardown.failed:
        if request.node.rep_teardown.failed:
            print("Test tear down has failed", request.node.nodeid)
            allure.attach(driver.get_screenshot_as_png(), name='TearDownScreenshot', attachment_type=AttachmentType.PNG)
