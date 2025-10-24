import pytest

# Lista con archivos de las pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_cart.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

# Ejecutar pytest con los argumentos definidos
pytest.main(pytest_args)