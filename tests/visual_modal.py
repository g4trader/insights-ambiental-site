import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def capture_modal_screenshot(output: Path = Path("modal-desktop.png")) -> Path:
    """
    Abre o site local (http://localhost:4173/) e captura um print
    da modal de serviços com Selenium em modo headless.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://localhost:4173/")

        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.ID, "servicos")))

        servicos = driver.find_element(By.ID, "servicos")
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});",
            servicos,
        )

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#servicos .group")))
        first_card = driver.find_elements(By.CSS_SELECTOR, "#servicos .group")[0]
        driver.execute_script("arguments[0].click();", first_card)

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-modal='true']")))
        time.sleep(1)
        driver.save_screenshot(str(output))
        return output
    finally:
        driver.quit()


if __name__ == "__main__":
    screenshot_path = capture_modal_screenshot()
    print(f"Screenshot salvo em: {screenshot_path.resolve()}")

