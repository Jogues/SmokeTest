from selenium import webdriver

def before_all(context):
  #context.browser = webdriver.Firefox()
  context.browser = webdriver.Chrome('D:\Data1\chromedriver')
  #context.browser = webdriver.PhantomJS()
  #context.browser = webdriver.

def after_all(context):
  context.browser.quit()

def before_feature(context, feature):
  context.browser = webdriver.Chrome('D:\Data1\chromedriver')
  #context.browser = webdriver.PhantomJS()
  #context.browser = webdriver.Firefox()

def after_feature(context, feature):
  context.browser.quit()
