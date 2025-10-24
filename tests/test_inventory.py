from selenium.webdriver.common.by import By
from selenium import webdriver

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver
        assert driver.title == "Swag Labs"

        products = driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(products) > 0, "No hay productos visibles en la página"
    except Exception as e:
        print(f"Error en el test_iventory: {e}")
        raise
    finally:
        driver.quit()