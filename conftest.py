import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from database import inventory
from utils.logger import setup_logger
from selenium.webdriver.chrome.service import Service

#service = Service("/usr/local/bin/chromedriver")

#driver = webdriver.Chrome(service=service, options=options)



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