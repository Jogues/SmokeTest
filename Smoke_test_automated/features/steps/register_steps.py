from behave import *
from pages import login_page, register_page


@given(u'user in register user page')
def step_impl(context):
  register_page.register_url(context)

@when(u'he register new user with "{email}" "{fullname}" "{username}" and "{password}"')
def step_impl(context, email, fullname, username, password):
  register_page.register_instructor(context, email, fullname, username, password)

@then(u'a new account should be created and user redirected to dashboard page')
def step_impl(context):
  login_page.arrive_in_dashboard(context)
