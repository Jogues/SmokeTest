from behave import *
from pages import login_page, student_see_details_page

# Scenario 1
@given(u'student are in Labster website')
def step_impl(context):
  login_page.login_url(context)

@when(u'they login into labster using their "{email}" & "{password}"')
def step_impl(context, email, password):
  login_page.login(context, email, password)
  login_page.arrive_in_dashboard(context)

@then(u'they should be able to see the course that they enroll with')
def step_impl(context):
  student_see_details_page.find_enroll_course(context)

# Scenario 2
@given(u'student already in dashboard page')
def step_impl(context):
  login_page.arrive_in_dashboard(context)

@when(u'they click on the CCX course')
def step_impl(context):
  student_see_details_page.click_on_course(context)

@then(u'they should be able to access the courseware, course info and theory tabs')
def step_impl(context):
  student_see_details_page.access_course_detail(context)
