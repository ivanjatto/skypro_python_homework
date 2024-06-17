from time import sleep
from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service as ChromeService # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

green_banner = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
    )
text = green_banner.text
print(text)
driver.quit()