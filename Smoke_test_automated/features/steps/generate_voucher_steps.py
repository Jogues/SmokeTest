from behave import *
from pages import generate_voucher_page

@given(u'Admin already inside API and access voucher menu')
def step_impl(context):
  generate_voucher_page.login_api_url(context)
  generate_voucher_page.login_api(context)

@when(u'he select the right license "{license}" and generated voucher')
def step_impl(context, license):
  generate_voucher_page.generate_voucher(context, license)

@then(u'the voucher for that specific license should be created')
def step_impl(context):
  generate_voucher_page.voucher_generated_success(context)
