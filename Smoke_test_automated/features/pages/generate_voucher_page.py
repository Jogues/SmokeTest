from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

#locators
apiLoginField = (By.ID, 'id_username')
apiPasswordField = (By.ID, 'id_password')
apiLoginButton = (By.CSS_SELECTOR, 'body > div > div > div > form > button')
licenseDropdownField = (By.ID, 'id_license')
voucherAmountField = (By.ID, 'id_count')
generateButton = (By.CSS_SELECTOR, 'body > div.container > div > div:nth-child(2) > form > button')

#data
usernameApi = ""
passwordApi = ""


def login_api_url(context):
  context.browser.get("https://api2.labster.com/vouchers/")

def login_api(context):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(apiLoginField))
  elem.clear()
  elem.send_keys(usernameApi)

  elem2 = wait.until(EC.visibility_of_element_located(apiPasswordField))
  elem2.clear()
  elem2.send_keys(passwordApi)

  elem3 = wait.until(EC.visibility_of_element_located(apiLoginButton))
  elem3.click()

def generate_voucher(context, license):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(licenseDropdownField))
  select = Select(elem)
  select.select_by_visible_text(license)
  time.sleep(5)

  elem2 = wait.until(EC.visibility_of_element_located(voucherAmountField))
  elem2.clear()
  elem2.send_keys("3")

  elem3 = wait.until(EC.visibility_of_element_located(generateButton))
  elem3.click()

def voucher_generated_success(context):
  pass
