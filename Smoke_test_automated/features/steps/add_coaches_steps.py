from behave import *
from pages import login_page, add_coach_page

@given(u'we have login into Labster as an admin using "{email}" and "{password}"')
def step_impl(context, email, password):
  login_page.login_url(context)
  login_page.login(context, email, password)

@when(u'we add new CCX coach "{instructorUsername}"')
def step_impl(context, instructorUsername):
  add_coach_page.add_instructor(context, instructorUsername)

@then(u'a new coach should be registered')
def step_impl(context):
  add_coach_page.successful_add_instructor(context)
