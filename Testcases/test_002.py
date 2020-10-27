from selenium.webdriver import Chrome

def test_regestration_data():
    path="C:/Users/User/PycharmProjects/jenkins/drivers/chromedriver_win32 (2)/chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www..com/")
    driver.maximize_window()

def test_regestration_invaliddata():
    path="C:/Users/User/PycharmProjects/jenkins/drivers/chromedriver_win32 (2)/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()