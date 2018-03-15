from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#locators
emailField = (By.ID, "register-email")
fullnameField = (By.ID, "register-name")
publicnameField = (By.ID, "register-username")
passwordField = (By.ID, "register-password")
iAgree = (By.XPATH, '//*[@id="register-honor_code"]')
createButton = (By.CSS_SELECTOR, "#register > button")
#urltest = "https://staging-courses-uk.labster.com/register?next=/dashboard" #staging UK Region
#urltest = "https://staging-courses.labster.com/register?next=/dashboard" #staging central region
#urltest = "https://courses-uk.labster.com/register?next=/dashboard" #production UK Region
urltest = "https://courses.labster.com/register?next=/dashboard" #production central region

def register_url(context):
  context.browser.get(urltest)

def register_instructor(context, email, fullname, username, password):
  wait = WebDriverWait(context.browser, 20)
  regEmail = wait.until(EC.visibility_of_element_located(emailField))
  regEmail.clear()
  regEmail.send_keys(email)
  regFullName = wait.until(EC.visibility_of_element_located(fullnameField))
  regFullName.clear()
  regFullName.send_keys(fullname)
  regPublicName = wait.until(EC.visibility_of_element_located(publicnameField))
  regPublicName.clear()
  regPublicName.send_keys(username)
  regPassword = wait.until(EC.visibility_of_element_located(passwordField))
  regPassword.clear()
  regPassword.send_keys(password)
  context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  regIAgree = wait.until(EC.element_to_be_clickable(iAgree))
  regIAgree.click()
  regCreate = wait.until(EC.visibility_of_element_located(createButton))
  regCreate.click()
