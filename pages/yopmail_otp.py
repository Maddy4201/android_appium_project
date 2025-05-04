import re

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

from selenium.webdriver.chrome.options import Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RZCXA1PTZJH"  # Replace with your actual device name
options.app_package = "com.android.chrome"
options.app_activity = "com.google.android.apps.chrome.Main"
options.automation_name = "UiAutomator2"

# Initialize Appium driver for Chrome
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(3)
# chose guest browser version
driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.chrome:id/signin_fre_dismiss_button']").click()
time.sleep(1)
# notification_no_thanks_button = "//android.widget.Button[@resource-id='com.android.chrome:id/negative_button']"
# chrome_notification_dont_allow_button = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"
# "//android.widget.Button[@resource-id='com.android.chrome:id/signin_fre_continue_button']"
# more button
try:
	driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.chrome:id/more_button']").click()
	time.sleep(1)
	# no thanks button
	# driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.chrome:id/button_secondary']").click()
	# time.sleep(1)
	#  got it button
	driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.chrome:id/ack_button']").click()
	time.sleep(1)
except Exception as e:
	print ("Exception occurred")

driver.get("https://www.yopmail.com")
time.sleep(2)
# Enter the Yopmail address and refresh
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='login']").send_keys("sjsjs123")  # Replace with your test email ID
time.sleep(1)
driver.find_element(AppiumBy.XPATH, "//android.view.View[@resource-id='refreshbut']").click()
time.sleep(2)
noOfEmails = driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text='Inbox']//android.view.View[./@resource-id and not(./android.widget.TextView[@text='today'])]")
if noOfEmails:
	noOfEmails[0].click()
time.sleep(2)
email_body_element = driver.find_element(AppiumBy.XPATH, "//android.widget.GridView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View")
email_body = email_body_element.text
# Extract 4-digit OTP using regex
otp_match = re.search(r"\b\d{4}\b", email_body)
print("The found OTP is: ",otp_match.group() if otp_match else "OTP not found")
time.sleep(5)
