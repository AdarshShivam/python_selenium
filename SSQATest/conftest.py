import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os

@pytest.fixture(scope="class")
def init_driver(request):
    pass
    supported_browsers = ['chrome','ch','headlesschrome','firefox','ff']
    browser = os.environ.get('BROWSER',None)
    if not browser:
        raise Exception("The Environment variable 'BROWSER' must be set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser {browser} is not supported"  
                        f"Supported Browsers are {supported_browsers}")

    if browser in ('chrome','ch'):
        driver = webdriver.Chrome()

    elif browser in ('firefox','ff'):
        driver = webdriver.Firefox()

    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

    request.cls.driver = driver
    yield
    # import pdb; pdb.set_trace()
    driver.quit()

# FUNCTION FOR REPORT CREATION
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            # extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            extra.append(pytest_html.extras.image(".images.jpg"))
        report.extra = extra