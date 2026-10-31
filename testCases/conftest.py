import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Lanzando navegador Chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Lanzando navegador Firefox")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Lanzando navegador Edge")
    else:
        raise pytest.UsageError(f"Browser '{browser}' no soportado")
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#PyTest HTML Report
#It is hook for addjun environment info to HTML Report
def pytest_metadata(metadata):
    metadata['Project Name'] = 'Python Orange'
    metadata['Module Name'] = 'Users'
    metadata['Tester'] = 'Nadia'

    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
