from behave import *
from pages import login_page, add_unenroll_student_page

# Scenario 1
@given(u'user login as instructor account with "{email}" & "{password}"')
def step_impl(context, email, password):
  login_page.login_url(context)
  login_page.login(context, email, password)

@when(u'accessing the right course')
def step_impl(context):
  add_unenroll_student_page.open_CCX_coach(context)

@when(u'the instructor add a valid email/username "{username}"')
def step_impl(context, username):
  add_unenroll_student_page.add_student_batch(context, username)

@then(u'the student "{username}" should be enroll into the course')
def step_impl(context, username):
  add_unenroll_student_page.successful_add_student(context, username)

#Scenario 2
@given(u'user already in CCX coach page')
def step_impl(context):
  pass

@when(u'the instructor unenroll a valid email/username "{username}"')
def step_impl(context, username):
  add_unenroll_student_page.unenroll_student_batch(context, username)

@then(u'the student should be no longer appear in the list')
def step_impl(context):
  add_unenroll_student_page.successful_remove_student(context)


#Scenario 3
@given(u'user already in CCX coach pages')
def step_impl(context):
  pass

@when(u'the instructor enroll a second valid email/username "{username}"')
def step_impl(context, username):
  add_unenroll_student_page.add_student_batch(context, username)

@then(u'the student "{username}" should be enroll into the right course')
def step_impl(context, username):
  add_unenroll_student_page.successful_add_student(context, username)
