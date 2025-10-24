# Proyecto de automatización de pruebas con Selenium y Pytest

El propósito de este proyecto automatizar pruebas funcionales de una aplicación web utilizando Selenium WebDriver y Pytest.  
Permite validar flujos de inicio de sesión, navegación y otras funcionalidades clave de forma rápida y repetible.

Tecnologías utilizadas
- Python
- Selenium para la automatización del navegador  
- Pytest como framework de ejecución de pruebas  
- Google Chrome como entorno de prueba principal


Instalación de Dependencias

1_ pip install selenium
2_ pip install pytest
3_ pip install pytest-html

Ejecución de las pruebas

Para ejecutar todos los casos de prueba: pytest -v
Para ejecutar de manera individual: 
pytest tests/test_login.py -v
pytest tests/test_inventory.py -v
pytest tests/test_cart.py -v 