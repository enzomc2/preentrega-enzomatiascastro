from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_cart(login_in_driver):
    try:
        driver = login_in_driver
        assert driver.title == "Swag Labs", "El título de la página no es el esperado"

        time.sleep(2)


        add_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
        add_button.click()


        time.sleep(1)
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1", "El contador del carrito no muestra el número esperado"


        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()


        time.sleep(2)
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 1, "El producto no se añadió correctamente al carrito"

        print("✅ Test de carrito completado exitosamente")

    except Exception as e:
        print(f"❌ Error en el test_cart: {e}")
        raise

    finally:
        driver.quit()