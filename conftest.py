import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='eng',
                     help='Choose language: eng, ru, etc')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        # chrome lang setting
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        # firefox lang setting
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)

        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox and user_language must be")
    yield browser
    print("\nquit browser..")
    browser.quit()
