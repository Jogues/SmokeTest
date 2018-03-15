from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


#locators
batchEnrollmentField = (By.ID, 'student-ids')
studentListManagementField = (By.ID, 'student-id')
enrollButton = (By.CSS_SELECTOR, '#membership > div.batch-enrollment > form > div:nth-child(7) > input:nth-child(1)')
unenrollButton = (By.CSS_SELECTOR, '#membership > div.batch-enrollment > form > div:nth-child(7) > input:nth-child(2)')
memberList = (By.CSS_SELECTOR, '#membership > div.member-lists-management > form > div > div > div.member-list')
addStudentButton = (By.CSS_SELECTOR, '#membership > div.member-lists-management > form > div > div > div.bottom-bar > input.add')
instructorCourse = (By.LINK_TEXT, 'Automated Course')
ccxCoachMenu = (By.LINK_TEXT, 'CCX Coach')


def open_CCX_coach(context):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(instructorCourse))
  elem.send_keys("\n")
  elem1 = wait.until(EC.visibility_of_element_located(ccxCoachMenu))
  elem1.click()
  time.sleep(5)
  context.browser.save_screenshot('before enroll student.png')

def add_student_batch (context, username):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(batchEnrollmentField))
  elem.clear()
  elem.send_keys(username)
  #click on the enroll button
  elem2 = wait.until(EC.visibility_of_element_located(enrollButton))
  elem2.send_keys("\n")
  time.sleep(5)
  context.browser.save_screenshot('after enroll student.png')

def unenroll_student_batch (context, username):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(batchEnrollmentField))
  elem.clear()
  elem.send_keys(username)
  #click on the unenroll button
  elem2 = wait.until(EC.visibility_of_element_located(unenrollButton))
  elem2.send_keys("\n")

def add_student_list_management (context, username):
  wait = WebDriverWait(context.browser, 20)
  elem = wait.until(EC.visibility_of_element_located(studentListManagementField))
  elem.clear()
  elem.send_keys(username)
  #click on add student button
  elem2 = wait.until(EC.visibility_of_element_located(addStudentButton))
  elem2.click()

def successful_add_student(context, username):
  wait = WebDriverWait(context.browser, 20)
  wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#membership > div.member-lists-management > form > div > div > div.member-list'), username))

def successful_remove_student(context):
  pass
