from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def drive_driver():
    global driver
    driver = webdriver.Edge(r"C:\Users\AnnishJK\Downloads\msedgedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    yield 
    driver.quit()

@pytest.mark.usefixtures("drive_driver")
def test_google():
    assert driver.title =="Google"

@pytest.mark.usefixtures("drive_driver")
def test_rediff():
    assert driver.current_url =="https://www.google.com/?gws_rd=ssl"
    