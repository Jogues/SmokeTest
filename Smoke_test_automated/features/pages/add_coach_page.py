from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver 
import time

#locators
instructorView = (By.LINK_TEXT, 'Instructor View')
instructorMenu = (By.LINK_TEXT, 'Instructor')
membershipMenu = (By.CSS_SELECTOR, '#instructor-dashboard-content > ul > li:nth-child(2) > a')
rCourseTeamRole = (By.ID, 'member-lists-selector')
rCcxCoaches = (By.CSS_SELECTOR, '#membership > div > div:nth-child(10)')
rEnterUsername = (By.ID, 'add-field')
addButton = (By.ID, '#membership > div > div.auth-list-container.active > div > div.bottom-bar > input')
autoEnrollButton = (By.CSS_SELECTOR, '#membership > fieldset.batch-beta-testers.membership-section > div:nth-child(3) > label > span')
body = (By.CSS_SELECTOR, '#membership > div > div.auth-list-container.active > div > div.member-list > table > tbody')

def add_instructor(context, instructorUsername):
  wait = WebDriverWait(context.browser, 20)
  # clicking the instructor menu
  elem = wait.until(EC.element_to_be_clickable(instructorView))
  elem.send_keys("\n")
  # clicking the instructor tab
  elem1 = wait.until(EC.visibility_of_element_located(instructorMenu))
  elem1.click()
  # selecting the membership tab
  elem2 = wait.until(EC.visibility_of_element_located(membershipMenu))
  elem2.click()
  # change the dropdown from staff to ccx coaches
  elem3 = wait.until(EC.visibility_of_element_located(rCourseTeamRole))
  select = Select(elem3)
  select.select_by_visible_text("CCX Coaches")
  #time.sleep(5)
  # scroll down the page list 
  """elem = context.browser.find_element_by_css_selector('#content > div')
  context.browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", elem)"""
  #context.browser.save_screenshot('before-add-coach.png')
  #input valid username or email
  ccxCoachAdd = context.browser.find_element_by_xpath('//*[@id="membership"]/div/div[9]')
  addCoach = ccxCoachAdd.find_element_by_id('add-field')
  addCoach.click()
  addCoach.send_keys(instructorUsername)
  # click add ccx coaches button
  addButtonClick = context.browser.find_element_by_xpath('//*[@id="membership"]/div/div[9]')
  RaddButton = addButtonClick.find_element_by_css_selector('#membership > div > div.auth-list-container.active > div > div.bottom-bar > input')
  RaddButton.click()

def successful_add_instructor(context):
  time.sleep(5)
  context.browser.save_screenshot('after-add-coach.png')
  #removing the newly add coach
