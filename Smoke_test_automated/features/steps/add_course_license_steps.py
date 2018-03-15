from behave import *
from pages import login_page, add_course_license_page


# SCENARIO 1
@given(u'Instructor already login to labster using "{email}" and "{password}"')
def step_impl(context, email, password):
  login_page.login_url(context)
  login_page.login(context, email, password)
  login_page.arrive_in_dashboard(context)

@when(u'they go to ccx coach menu and add "{course}" as a new course')
def step_impl(context, course):
  add_course_license_page.add_course(context, course)

@then(u'a new course should be created')
def step_impl(context):
  add_course_license_page.course_added(context)

# SCENARIO 2
@given(u'Instructor open the license tab')
def step_impl(context):
  add_course_license_page.open_license_tab(context)

@when(u'Instructor input the correct CK "{consumerKey}", SK "{secretKey}", and license code "{licCode}"')
def step_impl(context ,consumerKey, secretKey, licCode):
  add_course_license_page.add_license(context, consumerKey, secretKey, licCode)

@then(u'the license should applied correctly')
def step_impl(context):
  add_course_license_page.license_applied(context)
