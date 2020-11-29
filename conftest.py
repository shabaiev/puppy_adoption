import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--driver_folder", default="/Users/Ilya/PycharmProjects/puppy_adoption/drivers")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("browser")
    folder = request.config.getoption("driver_folder")
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{folder}/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{folder}/operadriver")
    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    request.addfinalizer(driver.close)
    driver.maximize_window()

    return driver
