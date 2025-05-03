from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy

# Define capabilities using AppiumOptions
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RZCXA1PTZJH"  # Your actual device name
options.app_package = "in.co.websites.websitesapp"
options.app_activity = "in.co.websites.websitesapp.main.MainActivity"
options.automation_name = "UiAutomator2"

# Start Appium session
driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(10)
# Wait for app to launch
# time.sleep(3)
element = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/btn_ok']")
element.click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/btn_sign_in']").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/email_login']").send_keys("scott904@yopmail.com")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/password_login']").send_keys("Testuser@29")
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/login_button']").click()
# allow after login
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']").click()
time.sleep(1)
# ignore you referral window
try:
	referral_pop = driver.find_element(AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='closeImage']")
	if referral_pop.is_displayed():
		referral_pop.click()
	else:
		print("Referral pop up not displayed")
except:
	print("Refrerral pop-up ignored")
# click on sidebar
driver.find_element(AppiumBy.XPATH,"//android.widget.ImageButton[@content-desc='Open']").click()
# click on buy subcription
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/material_drawer_name' and @text='Buy Subscription']").click()
driver.find_element(AppiumBy.XPATH,"(//android.widget.CheckBox[@content-desc='checkBox'])[1]").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Subscribe Now']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/packageBtn']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/pay_button']").click()

# sale_offer_pop_up = "//android.widget.ImageView[@resource-id='in.co.websites.websitesapp:id/close']"

# subscribe now button = //android.widget.TextView[@text='Subscribe Now']
# buy_subscription button = //android.widget.Button[@resource-id='in.co.websites.websitesapp:id/packageBtn']
# pay_button = //android.widget.Button[@resource-id='in.co.websites.websitesapp:id/pay_button']
# pay_with_card_button = //android.widget.TextView[@resource-id="in.co.websites.websitesapp:id/cardPayTextview"]

# Billing: //android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/material_drawer_name' and @text='Billing']

time.sleep(4)
print("App launched successfully!")

# Close the driver
# driver.quit()
