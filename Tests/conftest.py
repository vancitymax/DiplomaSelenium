import os
from datetime import datetime

import  pytest


from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name: chrome or firefox")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    print(f"Running test in {browser_name} browser")
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise TypeError(f"Browser {browser_name} is not supported")
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%Y%m%d-%H%M%S")+".html"