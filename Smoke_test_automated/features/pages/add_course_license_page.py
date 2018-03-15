from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


#locators
instructorView = (By.LINK_TEXT, 'Instructor View')
ccxCoachMenu = (By.LINK_TEXT, 'CCX Coach')
licenseMenu = (By.LINK_TEXT, 'License')
inputCCX = (By.ID, 'ccx_name')
inputCCXButton = (By.CSS_SELECTOR, '#create-ccx')
scheduleTab = (By.LINK_TEXT, 'Schedule')
inputCK = (By.ID, 'labster-consumer')
inputSK = (By.ID, 'labster-secret')
inputlic = (By.ID, 'labster-license')
applyLicButton = (By.CSS_SELECTOR, '#labster-license-dashboard-content > form:nth-child(2) > p:nth-child(5) > button:nth-child(1)')


def add_course(context, course):
  wait = WebDriverWait(context.browser, 20)
  # clicking instructor view
  elem = wait.until(EC.visibility_of_element_located(instructorView))
  elem.click()
  # clicking ccx coach menu
  elem1 = wait.until(EC.visibility_of_element_located(ccxCoachMenu))
  elem1.click()
  #inputing new course name
  elem2 = wait.until(EC.visibility_of_element_located(inputCCX))
  elem2.clear()
  elem2.send_keys(course)
  #clicking create course button
  elem3 = wait.until(EC.visibility_of_element_located(inputCCXButton))
  elem3.click()

def course_added(context):
  pass
  """wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(scheduleTab))
  elem.click()"""

def open_license_tab(context):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(licenseMenu))
  elem.click()

def add_license(context, consumerKey, secretKey, licCode):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(inputCK))
  elem.clear()
  elem.send_keys(consumerKey)

  elem1 = wait.until(EC.visibility_of_element_located(inputSK))
  elem1.clear()
  elem1.send_keys(secretKey)

  elem2 = wait.until(EC.visibility_of_element_located(inputlic))
  elem2.clear()
  elem2.send_keys(licCode)

  elem3 = wait.until(EC.visibility_of_element_located(applyLicButton))
  elem3.click()

def license_applied(context):
  pass
