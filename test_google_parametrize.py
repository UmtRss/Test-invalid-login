import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 🔧 Tarayıcı setup
@pytest.fixture
def browser():
    print("\n[SETUP] Tarayıcı başlatılıyor...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("\n[TEARDOWN] Tarayıcı kapatılıyor...")
    driver.quit()

# 📊 Parametrize: 3 arama kelimesiyle testi döndür
@pytest.mark.parametrize("keyword", ["ChatGPT", "OpenAI", "Python"])
def test_google_search_multiple_keywords(browser, keyword):
    browser.get("https://www.google.com")

    # Çerez popup'ını geç
    try:
        accept_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Kabul ediyorum')]")
        accept_button.click()
    except:
        pass

    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)

    time.sleep(2)
    assert keyword.lower() in browser.title.lower()
