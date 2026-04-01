import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import logging
from utils import logger

logger.setup_logger()

# Import DB functions
from  database import inventory

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")



# Create table once
inventory.create_table()

driver = webdriver.Chrome(options=options)

try:
    driver.maximize_window()
    driver.get("https://sauce-demo.myshopify.com/")

    wait = WebDriverWait(driver, 20)

    catalog_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='main-menu']//a[text()='Catalog']"))
    )
    catalog_btn.click()

    time.sleep(5)

    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "four")))
    products = driver.find_elements(By.CLASS_NAME, "four")

    for product in products:
        name = product.find_element(By.TAG_NAME, "h3").text
        price = product.find_element(By.TAG_NAME, "h4").text

        price = float(price.replace("£", "").strip())
        image_url = product.find_element(By.TAG_NAME, "img").get_attribute("src")
        product_url = product.find_element(By.TAG_NAME, "a").get_attribute("href")

        status = "In Stock"

        inventory.insert_product(name, price, status, image_url, product_url)

        #print(f"Saved: {name} - {price}")
        logging.info("Catalog button clicked successfully!")
        logging.info(f"Saved: {name} - {price}")
        logging.error("Timeout: Page didn't load in time")
        #logging.error(f"Unexpected error: {e}")

except TimeoutException:
    print("Timeout: Page didn't load in time")

except NoSuchElementException:
    print("Element not found!")

except Exception as e:
    print("Unexpected error:", e)

finally:
    driver.quit()

def setup_logger():
    logging.basicConfig(
        filename='scraper.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

from database import check_db

check_db.check_products()