from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    URL = "https://sauce-demo.myshopify.com/"

    CATALOG_BTN = (By.XPATH, "//*[@id='main-menu']//a[text()='Catalog']")
    PRODUCTS = (By.CSS_SELECTOR, ".product-grid > div")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 35)

    def open(self):
        self.driver.get(self.URL)

    def go_to_catalog(self):
        self.wait.until(EC.presence_of_element_located(self.CATALOG_BTN))
        self.wait.until(EC.element_to_be_clickable(self.CATALOG_BTN)).click()

    def get_products(self):
        product_elements = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCTS)
        )

        products_data = []
        self.driver.save_screenshot("debug.png")
        for product in product_elements:
            name = product.find_element(By.TAG_NAME, "h3").text

            price = product.find_element(By.TAG_NAME, "h4").text
            #price = float(price.replace("£", "").strip())

            image_url = product.find_element(By.TAG_NAME, "img").get_attribute("src")
            product_url = product.find_element(By.TAG_NAME, "a").get_attribute("href")

            products_data.append((name, price, "In Stock", image_url, product_url))
            self.driver.save_screenshot("debug.png")
        return products_data