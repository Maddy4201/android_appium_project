from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy

# Define capabilities using AppiumOptions
from appium.options.android import UiAutomator2Options

from pages.base_page import BasePage


class UserLogin(BasePage):


	def __init__(self):
		super().__init__()

# Wait for app to launch
# time.sleep(3)
	def user_login(self):
		element = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/btn_ok']")
		element.click()
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']").click()
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']").click()
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/btn_sign_in']").click()
		self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/email_login']").send_keys("scott904@yopmail.com")
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/password_login']").send_keys("Testuser@29")
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/login_button']").click()
		# allow after login
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']").click()
		time.sleep(1)
		# ignore you referral window
		try:
			referral_pop = self.driver.find_element(AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='closeImage']")
			if referral_pop.is_displayed():
				referral_pop.click()
			else:
				print("Referral pop up not displayed")
		except:
			print("Refrerral pop-up ignored")
		# click on sidebar
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.ImageButton[@content-desc='Open']").click()
		# click on buy subcription
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/material_drawer_name' and @text='Buy Subscription']").click()
		self.driver.find_element(AppiumBy.XPATH,"(//android.widget.CheckBox[@content-desc='checkBox'])[1]").click()
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Subscribe Now']").click()
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/packageBtn']").click()
		self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/pay_button']").click()

if __name__ == "__main__":
	user = UserLogin()
	user.user_login()


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
