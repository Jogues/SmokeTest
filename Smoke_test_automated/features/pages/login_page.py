from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#locators
LoginButton = (By.CSS_SELECTOR, '#menu-item-5098 > a')
InputEmail = (By.ID, 'login-email')
InputPassword = (By.ID, 'login-password')
SignInButton = (By.CSS_SELECTOR, '#login > button')
SearchInDashboard = (By.CSS_SELECTOR, "#dashboard-search-bar > form > label")
errorInLogin = (By.CSS_SELECTOR, "#login-form > div:nth-child(2) > div.status.submission-error > h4")
#urltest = "https://staging-courses-uk.labster.com/login?next=/dashboard" #staging UK Region
#urltest = "https://staging-courses.labster.com/login?next=/dashboard" #staging central region
#urltest = "https://courses-uk.labster.com/login?next=/dashboard" #production UK Region
urltest = "https://courses.labster.com/login?next=/dashboard" #production central region


def login_url(context):
  context.browser.get(urltest)

def login(context, email, password):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(InputEmail))
  elem.send_keys(email)
  elem1 = wait.until(EC.visibility_of_element_located(InputPassword))
  elem1.send_keys(password)
  elem2 = wait.until(EC.visibility_of_element_located(SignInButton))
  elem2.click()

def arrive_in_dashboard(context):
  wait = WebDriverWait(context.browser, 20)
  wait.until(EC.visibility_of_element_located(SearchInDashboard))

def login_error(context):
	wait = WebDriverWait(context.browser, 20)
	wait.until(EC.text_to_be_present_in_element((errorInLogin), "We couldn't sign you in."))
