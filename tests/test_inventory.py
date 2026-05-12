import logging
from pages.inventory_pages import InventoryPage
from database import inventory
from database import check_db
import allure
import pytest

@pytest.mark.regression
def test_scrape_and_store_products(driver):
    page = InventoryPage(driver)

    page.open()
    page.go_to_catalog()

    products = page.get_products()

    assert len(products) > 0, "No products found!"

    for product in products:
        inventory.insert_product(*product)
        logging.info(f"Inserted: {product[0]}")

    # DB Validation
    db_products = inventory.get_all_products()

    assert len(db_products) > 0, "No data in database!"

check_db.check_products()

@allure.title("Verify products availability")
@allure.description("Checks whether products available")

@pytest.mark.smoke
def test_login():
    pass