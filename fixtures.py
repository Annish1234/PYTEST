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

def test_google(drive_driver):
    assert driver.title =="Google"

