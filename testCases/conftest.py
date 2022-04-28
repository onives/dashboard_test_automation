import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# generate pytest html report
def pytest_configure(config):
    config.metadata['Project Name'] = 'Nives Dashboard'
    config.metadata['Module Name'] = 'Admins'
    config.metadata['Tester'] = 'Nives'


# Hook for delete/modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
