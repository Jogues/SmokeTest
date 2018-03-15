from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select 
import time
    
#locators
enterAccessCodeMenu = (By.CSS_SELECTOR, '#global-navigation > nav > ol.left.nav-global.list-inline.authenticated > li:nth-child(2) > a')
enterAccessCodeField = (By.ID, 'code')
enterAccessCodeButton = (By.CSS_SELECTOR, '#submit')
myCourses = (By.ID, 'my-courses')
dashboardField = (By.ID, 'dashboard-search-input')

def access_voucher_menu(context):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(enterAccessCodeMenu))
  elem.click()

def use_voucher_code(context, voucherCode):
  wait = WebDriverWait(context.browser, 20)
  elem1 = wait.until(EC.visibility_of_element_located(enterAccessCodeField))
  elem1.clear()
  elem1.send_keys(voucherCode)

  elem2 = wait.until(EC.visibility_of_element_located(enterAccessCodeButton))
  elem2.click()

  #elem3 = wait.until(EC.visibility_of_element_located(dashboardField))
  """elem3 = context.browser.find_element_by_id('dashboard-search-input')
  if elem3.is_displayed():
  	return True
  else:
  	print("There is an error when you applied the voucher code")
	context.browser.save_screenshot("error_voucher.png")
	return False"""

def enroll_via_voucher(context):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(myCourses))
