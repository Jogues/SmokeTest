from behave import *
from pages import login_page

@given(u'user is on login page')
def step_impl(context):
  login_page.login_url(context)

@when(u'I login with "{username}" and "{password}"')
def step_impl(context, username, password):
  login_page.login(context, username, password)

@then(u'I am on the Dashboard page')
def step_impl(context):
  login_page.arrive_in_dashboard(context)

@then(u'I will have an error')
def step_impl(context):
  login_page.login_error(context)
