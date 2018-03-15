from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

#locators
settingButton = (By.CSS_SELECTOR, '#actions-dropdown-link-0 > span.fa.fa-cog')
myCoursesLink = (By.LINK_TEXT, 'Automated Course')
myCourses = (By.ID, 'my-courses')
dropdownUnenroll = (By.CSS_SELECTOR, '#unenroll-0')
unenrollButton = (By.CSS_SELECTOR, '#unenroll_form > div > input[type="submit"]')


def courses_available(context):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(myCoursesLink))

def unenroll_from_course(context):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(settingButton))
  elem.click()

  elem2 = wait.until(EC.visibility_of_element_located(dropdownUnenroll))
  elem2.click()
  time.sleep(3)

  elem3 = wait.until(EC.visibility_of_element_located(unenrollButton))
  elem3.click()

def successfully_unenroll_student(context):
  time.sleep(3)
  context.browser.save_screenshot('student unenroll from automated course.png')
