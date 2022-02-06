from selenium import webdriver


def test_google():
    driver = webdriver.Edge(r"C:\Users\AnnishJK\Downloads\msedgedriver.exe")
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_gmail():
    driver = webdriver.Edge(r"C:\Users\AnnishJK\Downloads\msedgedriver.exe")
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    assert driver.title == "Gmail"
    driver.quit()

def test_insta():
    driver = webdriver.Edge(r"C:\Users\AnnishJK\Downloads\msedgedriver.exe")
    driver.get("https://www.instagram.com/")
    assert driver.title == "Instagram"
    driver.quit()


def test_rediff():
    driver = webdriver.Edge(r"C:\Users\AnnishJK\Downloads\msedgedriver.exe")
    driver.get("https://www.rediff.com/")
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()