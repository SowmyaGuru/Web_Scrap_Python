import requests
import pytest
import allure

response = requests.get("https://sauce-demo.myshopify.com/products.json")
data = response.json()

@allure.feature("Products API")
@allure.story("Validate product status API test1")
@allure.id("test1")
@pytest.mark.smoke
@pytest.mark.api
def test_products_api():

     for i , product in enumerate(data["products"],start=1):

         title = product["title"]
         price = product["variants"][0]["price"]

         print(f"{i}.{title}")
         print(f"Price:  ${price}")
         print("------------------------------------")
     assert response.status_code == 200

@allure.id("test2")
@pytest.mark.smoke
@pytest.mark.api
def test_product_count():

     assert len(data["products"]) > 0

