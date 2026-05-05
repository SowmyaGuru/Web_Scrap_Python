import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from database import inventory
from utils.logger import setup_logger

@pytest.fixture(scope="session", autouse=True)
def setup():
    setup_logger()
    inventory.create_table()


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()