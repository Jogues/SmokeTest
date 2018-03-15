from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

#locators
courseEnroll = (By.LINK_TEXT, 'Automated Course')
homeTab = (By.LINK_TEXT, 'Home')
simulationTab = (By.LINK_TEXT, 'Simulations')
theoryTab = (By.LINK_TEXT, 'Theory')
bookmarkButton = (By.CSS_SELECTOR, '#content > div.container > div > div > div.wrapper-course-modes > div > button')



def find_enroll_course(context):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(courseEnroll))

def click_on_course(context):
  wait = WebDriverWait(context.browser, 20)
  elem1 = wait.until(EC.visibility_of_element_located(courseEnroll))
  elem1.click()

def access_course_detail(context):
  wait = WebDriverWait(context.browser, 20)
  elem2 = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#main > div > div.home > div > h2'), 'Instructor View'))

  elem3 = wait.until(EC.visibility_of_element_located(simulationTab))
  elem3.click()
  elem4 = wait.until(EC.visibility_of_element_located(bookmarkButton))

  elem5 = wait.until(EC.visibility_of_element_located(theoryTab))
  elem5.click()
  elem6 = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#article-title'), 'Welcome to the Labster Theory Pages'))
