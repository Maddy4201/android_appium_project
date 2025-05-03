from appium import webdriver
from appium.options.android import UiAutomator2Options

class BasePage:
    def __init__(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "RZCXA1PTZJH"
        options.app_package = "in.co.websites.websitesapp"
        options.app_activity = "in.co.websites.websitesapp.main.MainActivity"
        options.automation_name = "UiAutomator2"

        self.driver = webdriver.Remote("http://localhost:4723", options=options)
        self.driver.implicitly_wait(10)
