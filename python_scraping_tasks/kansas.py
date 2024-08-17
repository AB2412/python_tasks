from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
import json


import time
import pdb

def run_script():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  captcha_request(driver)
  time.sleep(20)
  driver.get("https://kboc.kansas.gov/api/?CodeClass/LIC_TYPE")
  with open('file.html', 'w', encoding='utf-8') as file:
      file.write(driver.page_source)
  # pdb.set_trace()
  captcha_request(driver)
  time.sleep(30)
  code_values = get_code_values()
  pdb.set_trace()
  driver.execute_script("document.getElementById('prac_lic_type').value = '149026';")
  # Enter the License Number
  license_number_field = driver.find_element(By.ID, "prac_lic_no")
  license_number_field.send_keys("000-25135")

  # Click the Search button
  driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
  # Wait for the results page to load
  time.sleep(5)
  with open('000-25135.html', 'w', encoding='utf-8') as file:
      file.write(driver.page_source)


  # Save the page source as an HTML file

def get_code_values():
  with open("file.html", "r", encoding="utf-8") as file:
    html_content = file.read()
  soup = BeautifulSoup(html_content, 'html.parser')
  json_data = soup.find('pre').text
  data = json.loads(json_data)
  return [item['CODE_VALUE'] for item in data['CodeValues']]

def captcha_request(driver):
  driver.get("https://kboc.kansas.gov/verify/")
  WebDriverWait(driver, 10).until(
      EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]"))
  )
  # Locate the reCAPTCHA checkbox
  recaptcha_checkbox = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
  )
  recaptcha_checkbox.click()

run_script()