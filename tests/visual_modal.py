import subprocess
import sys
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
    Sobe um servidor HTTP simples (porta 4173), abre o site
    e captura um print da modal de serviços com Selenium.
    """
    project_root = Path(__file__).resolve().parents[1]
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", "4173"],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(1.5)

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
        server.terminate()
        try:
            server.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server.kill()


if __name__ == "__main__":
    screenshot_path = capture_modal_screenshot()
    print(f"Screenshot salvo em: {screenshot_path.resolve()}")

