from behave import *
from pages import login_page, use_voucher_page

@given(u'student login into Labster using their "{email}" & "{password}"')
def step_impl(context, email, password):
  login_page.login_url(context)
  login_page.login(context, email, password)
  login_page.arrive_in_dashboard(context)

@when(u'they arrived in dashboard and click on enter access code')
def step_impl(context):
  use_voucher_page.access_voucher_menu(context)

@when(u'input the voucher code "{voucherCode}"')
def step_impl(context, voucherCode):
  use_voucher_page.use_voucher_code(context, voucherCode)

@then(u'they should be enroll correctly into the right course')
def step_impl(context):
  use_voucher_page.enroll_via_voucher(context)