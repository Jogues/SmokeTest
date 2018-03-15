from behave import *
from pages import login_page, student_unenroll_page

@given(u'student login into labster using "{email}" & "{password}"')
def step_impl(context, email, password):
  login_page.login_url(context)
  login_page.login(context, email, password)
  login_page.arrive_in_dashboard(context)

@when(u'he arrive in dashboard and check that the courses that he want to unenroll is present')
def step_impl(context):
  student_unenroll_page.courses_available(context)

@when(u'click setting button and unenroll from course')
def step_impl(context):
  student_unenroll_page.unenroll_from_course(context)

@then(u'he should be successfully unenroll from that course')
def step_impl(context):
  student_unenroll_page.successfully_unenroll_student(context)
