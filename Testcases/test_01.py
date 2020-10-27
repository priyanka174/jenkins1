from selenium.webdriver import Chrome

def test_regestration_data():
    path= "/drivers/chromedriver_win32 (2)/chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.youtube.com/")
    driver.maximize_window()

def test_regestration_invaliddata():
    path= "/drivers/chromedriver_win32 (2)/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()

def test_regestration_invaliddata1():
    path = "/drivers/chromedriver_win32 (2)/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.google.com/")
    driver.maximize_window()