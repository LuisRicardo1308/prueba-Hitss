from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del navegador
options = Options()
options.add_argument("--start-maximized")  # Maximiza la ventana

driver = webdriver.Chrome(options=options)

try:
    # Paso 1: Ir al sitio principal
    driver.get("https://www.mercadolibre.com")

    # Paso 2: Seleccionar región México
    mexico_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "México"))
    )
    mexico_link.click()

    # Paso 3: Buscar "PlayStation 5"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "as_word"))
    )
    search_box.send_keys("PlayStation 5")
    search_box.send_keys(Keys.RETURN)

    # Paso 4: Aplicar filtro "Nuevo"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "as_word"))
    )
    search_box.send_keys(" Nuevo")
    search_box.send_keys(Keys.RETURN)

    # Paso 5: Filtrar por ubicación "CDMX"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "as_word"))
    )
    search_box.send_keys(" en Distrito Federal")
    search_box.send_keys(Keys.RETURN)

    # Paso 6: Ordenar por "Mayor precio"
    order_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "andes-dropdown__trigger"))
    )
    order_dropdown.click()

    high_to_low = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Mayor precio')]"))
    )
    high_to_low.click()

    time.sleep(3)

    # Paso 7: Extraer los primeros 5 productos (nombre y precio)
    items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ui-search-result__wrapper"))
    )

    print("\nTop 5 productos:\n")

    for item in items[:5]:
        try:
            title = item.find_element(By.CSS_SELECTOR, "h2").text
            price = item.find_element(By.CSS_SELECTOR, ".ui-search-price__second-line .andes-money-amount__fraction").text
            print(f"{title} - ${price}")
        except:
            continue

finally:
    time.sleep(5)  # Ver resultados antes de cerrar
    driver.quit()