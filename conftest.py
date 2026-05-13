import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from database import inventory
from utils.logger import setup_logger
import allure
from utils.utility_Screenshots import take_screenshot

@pytest.fixture(scope="session", autouse=True)
def setup():
    setup_logger()
    inventory.create_table()


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_path = take_screenshot(driver)

            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )