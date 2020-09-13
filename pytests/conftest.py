import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\Ravisha\\Desktop\\drivers\\geckodriver.exe")
    else:
        print('enter valid browser name')

    driver.get('http://localhost/login.do;jsessionid=33k7b2dfqbvm2')
    driver.implicitly_wait(10)
    request.cls.driver = driver  # returning cls.driver
    yield
    driver.quit()
