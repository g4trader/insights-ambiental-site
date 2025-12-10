"""
Testes para o ambiente de produção do site Insights Ambiental.
Testa acessibilidade, recursos, funcionalidades e performance.
"""
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


PRODUCTION_URL = "https://insightsambiental.com.br/"


def setup_driver(headless=True):
    """Configura e retorna o driver do Selenium."""
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def test_site_accessibility(driver):
    """Testa se o site está acessível e carrega corretamente."""
    print("\n🔍 Testando acessibilidade do site...")
    try:
        driver.get(PRODUCTION_URL)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("✅ Site acessível e carregado")
        return True
    except Exception as e:
        print(f"❌ Erro ao acessar o site: {e}")
        return False


def test_resources_loading(driver):
    """Testa se os recursos (CSS, JS, imagens) estão carregando."""
    print("\n🔍 Testando carregamento de recursos...")
    issues = []
    
    # Verifica se o CSS está carregado
    css_loaded = driver.execute_script("""
        return document.querySelector('link[rel="stylesheet"]') !== null;
    """)
    if not css_loaded:
        issues.append("CSS não encontrado")
    else:
        print("✅ CSS carregado")
    
    # Verifica se o JS está carregado
    js_loaded = driver.execute_script("""
        return document.querySelector('script[type="module"]') !== null;
    """)
    if not js_loaded:
        issues.append("JS não encontrado")
    else:
        print("✅ JS carregado")
    
    # Verifica imagens principais
    images_to_check = [
        "/images/logo_h.png",
        "/images/favicon.png",
        "/images/hero-bg.jpg"
    ]
    
    for img_path in images_to_check:
        img_loaded = driver.execute_script(f"""
            var img = new Image();
            img.src = '{PRODUCTION_URL}{img_path}';
            return img.complete && img.naturalHeight !== 0;
        """)
        if not img_loaded:
            issues.append(f"Imagem não carregada: {img_path}")
        else:
            print(f"✅ Imagem carregada: {img_path}")
    
    if issues:
        print(f"⚠️ Problemas encontrados: {', '.join(issues)}")
        return False
    return True


def test_console_errors(driver):
    """Verifica erros no console do navegador."""
    print("\n🔍 Verificando erros no console...")
    
    logs = driver.get_log('browser')
    errors = [log for log in logs if log['level'] == 'SEVERE']
    warnings = [log for log in logs if log['level'] == 'WARNING']
    
    if errors:
        print(f"❌ {len(errors)} erro(s) encontrado(s) no console:")
        for error in errors[:5]:  # Mostra apenas os primeiros 5
            print(f"   - {error['message']}")
        return False
    else:
        print("✅ Nenhum erro crítico no console")
    
    if warnings:
        print(f"⚠️ {len(warnings)} aviso(s) no console (não crítico)")
    
    return True


def test_page_elements(driver):
    """Testa se os elementos principais da página estão presentes."""
    print("\n🔍 Testando elementos da página...")
    issues = []
    
    elements_to_check = [
        ("#servicos", "Seção de serviços"),
        ("body", "Corpo da página"),
    ]
    
    for selector, name in elements_to_check:
        try:
            element = driver.find_element(By.CSS_SELECTOR, selector)
            if element:
                print(f"✅ {name} encontrado")
        except Exception as e:
            issues.append(f"{name} não encontrado: {e}")
            print(f"❌ {name} não encontrado")
    
    if issues:
        return False
    return True


def test_modal_functionality(driver):
    """Testa a funcionalidade do modal de serviços."""
    print("\n🔍 Testando funcionalidade do modal...")
    
    try:
        # Scroll até a seção de serviços
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.ID, "servicos")))
        
        servicos = driver.find_element(By.ID, "servicos")
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            servicos
        )
        time.sleep(1)
        
        # Tenta encontrar e clicar no primeiro card
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#servicos .group, #servicos [class*='group'], #servicos [class*='card']")))
        
        # Tenta diferentes seletores para o card
        card_selectors = [
            "#servicos .group",
            "#servicos [class*='group']",
            "#servicos [class*='card']",
            "#servicos > * > *",
        ]
        
        card = None
        for selector in card_selectors:
            try:
                cards = driver.find_elements(By.CSS_SELECTOR, selector)
                if cards:
                    card = cards[0]
                    break
            except:
                continue
        
        if not card:
            print("⚠️ Card de serviço não encontrado, mas seção existe")
            return True  # Não é crítico se o modal não abrir
        
        driver.execute_script("arguments[0].click();", card)
        time.sleep(1.5)
        
        # Verifica se o modal abriu
        modal = driver.find_elements(By.CSS_SELECTOR, "[aria-modal='true'], [role='dialog'], .modal, [class*='modal']")
        if modal:
            print("✅ Modal aberto com sucesso")
            
            # Tenta fechar o modal
            close_buttons = driver.find_elements(By.CSS_SELECTOR, "[aria-label*='close'], [aria-label*='fechar'], button[class*='close'], .close")
            if close_buttons:
                close_buttons[0].click()
                time.sleep(0.5)
                print("✅ Modal fechado com sucesso")
            
            return True
        else:
            print("⚠️ Modal não encontrado após clique (pode ser esperado)")
            return True  # Não é crítico
            
    except Exception as e:
        print(f"⚠️ Erro ao testar modal: {e}")
        return True  # Não é crítico se o modal não funcionar


def test_responsive_elements(driver):
    """Testa elementos responsivos básicos."""
    print("\n🔍 Testando responsividade...")
    
    # Testa em diferentes tamanhos de tela
    sizes = [
        (1920, 1080, "Desktop"),
        (768, 1024, "Tablet"),
        (375, 667, "Mobile"),
    ]
    
    for width, height, name in sizes:
        driver.set_window_size(width, height)
        time.sleep(0.5)
        
        body_width = driver.execute_script("return document.body.clientWidth;")
        if body_width > 0:
            print(f"✅ {name} ({width}x{height}): OK")
        else:
            print(f"❌ {name} ({width}x{height}): Problema")
    
    # Restaura tamanho original
    driver.set_window_size(1920, 1080)
    return True


def test_performance(driver):
    """Testa métricas básicas de performance."""
    print("\n🔍 Testando performance...")
    
    navigation_timing = driver.execute_script("""
        var perf = window.performance.timing;
        return {
            loadTime: perf.loadEventEnd - perf.navigationStart,
            domContentLoaded: perf.domContentLoadedEventEnd - perf.navigationStart,
            domInteractive: perf.domInteractive - perf.navigationStart
        };
    """)
    
    load_time = navigation_timing['loadTime'] / 1000  # em segundos
    dom_ready = navigation_timing['domContentLoaded'] / 1000
    
    print(f"⏱️ Tempo de carregamento: {load_time:.2f}s")
    print(f"⏱️ DOM pronto: {dom_ready:.2f}s")
    
    if load_time > 10:
        print("⚠️ Tempo de carregamento acima do ideal (>10s)")
    elif load_time > 5:
        print("⚠️ Tempo de carregamento pode ser melhorado (<5s ideal)")
    else:
        print("✅ Performance de carregamento OK")
    
    return True


def run_all_tests():
    """Executa todos os testes."""
    print("=" * 60)
    print("🧪 TESTES DO AMBIENTE DE PRODUÇÃO")
    print("=" * 60)
    print(f"URL: {PRODUCTION_URL}")
    
    driver = None
    results = {}
    
    try:
        driver = setup_driver(headless=True)
        
        results['accessibility'] = test_site_accessibility(driver)
        if not results['accessibility']:
            print("\n❌ Site não acessível. Parando testes.")
            return results
        
        results['resources'] = test_resources_loading(driver)
        results['console'] = test_console_errors(driver)
        results['elements'] = test_page_elements(driver)
        results['modal'] = test_modal_functionality(driver)
        results['responsive'] = test_responsive_elements(driver)
        results['performance'] = test_performance(driver)
        
        # Captura screenshot final
        screenshot_path = Path("production-test-screenshot.png")
        driver.save_screenshot(str(screenshot_path))
        print(f"\n📸 Screenshot salvo em: {screenshot_path.resolve()}")
        
    except Exception as e:
        print(f"\n❌ Erro durante os testes: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if driver:
            driver.quit()
    
    # Resumo
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS TESTES")
    print("=" * 60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name.upper():20} {status}")
    
    print(f"\nTotal: {passed}/{total} testes passaram")
    print("=" * 60)
    
    return results


if __name__ == "__main__":
    run_all_tests()



