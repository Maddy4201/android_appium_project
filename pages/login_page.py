from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy

# Define capabilities using AppiumOptions
from appium.options.android import UiAutomator2Options
from pages.base_page import BasePage

class UserLogin(BasePage):

	initial_permission_xpath = "//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/btn_ok']"
	location_access_xpath = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"
	allow_call_access_xpath = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"
	sign_in_button_xpath = "//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/btn_sign_in']"
	email_field_xpath = "//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/email_login']"
	password_field_xpath = "//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/password_login']"
	login_button_xpath = "//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/login_button']"
	allow_notification_after_login_xpath = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"
	referral_pop_up_xpath = "//android.widget.ImageView[@content-desc='closeImage']"
	sale_offer_pop_up_xpath = "//android.widget.ImageView[@resource-id='in.co.websites.websitesapp:id/close']"
	menu_side_bar_xpath = "//android.widget.ImageButton[@content-desc='Open']"
	buy_subscription_xpath = "//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/material_drawer_name' and @text='Buy Subscription']"
	monthly_subscription_xpath = "(//android.widget.CheckBox[@content-desc='checkBox'])[1]"
	subscribe_now_button_xpath = "//android.widget.TextView[@text='Subscribe Now']"
	confirm_plan_xpath = "//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/packageBtn']"
	confirm_payment_button_xpath = "//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/pay_button']"
	pay_with_card_button_xpath = "//android.widget.TextView[ @ resource - id = 'in.co.websites.websitesapp:id/cardPayTextview']"

	def __init__(self):
		super().__init__()

# Wait for app to launch
# time.sleep(3)
	def accept_permissions (self):
		self.driver.find_element(AppiumBy.XPATH, self.initial_permission_xpath).click()
		self.driver.find_element(AppiumBy.XPATH, self.location_access_xpath).click()
		self.driver.find_element(AppiumBy.XPATH, self.allow_call_access_xpath).click()
		time.sleep(1)

	def click_sign_in_button(self):
		self.driver.find_element(AppiumBy.XPATH, self.sign_in_button_xpath).click()

	def enter_user_email(self):
		self.driver.find_element(AppiumBy.XPATH, self.email_field_xpath).send_keys("miles604@yopmail.com")

	def enter_user_password(self):
		self.driver.find_element(AppiumBy.XPATH, self.password_field_xpath).send_keys("Testuser@17")

	def click_login_in_button(self):
		self.driver.find_element(AppiumBy.XPATH, self.login_button_xpath).click()
		# allow after login
	def ignore_post_login_popups(self):
		# ignore referral pop-up
		try:
			self.driver.find_element(AppiumBy.XPATH, self.allow_notification_after_login_xpath).click()
			time.sleep(2)
			self.driver.find_element(AppiumBy.XPATH, self.sale_offer_pop_up_xpath).click()
			referral_pop = self.driver.find_element(AppiumBy.XPATH, self.referral_pop_up_xpath)
			if referral_pop.is_displayed():
				referral_pop.click()
			else:
				print("Referral pop up not displayed")
		except:
			print("Referral pop-up ignored")

	def click_menu_sidebar(self):
		self.driver.find_element(AppiumBy.XPATH, self.menu_side_bar_xpath).click()

	def buy_subscription(self):
		# click on buy subscription
		self.driver.find_element(AppiumBy.XPATH, self.buy_subscription_xpath).click()
		self.driver.find_element(AppiumBy.XPATH, self.monthly_subscription_xpath).click()
		self.driver.find_element(AppiumBy.XPATH, self.subscribe_now_button_xpath).click()
		self.driver.find_element(AppiumBy.XPATH, self.confirm_plan_xpath).click()
		self.driver.find_element(AppiumBy.XPATH, self.confirm_payment_button_xpath).click()
		time.sleep(1)
		self.driver.find_element(AppiumBy.XPATH, self.pay_with_card_button_xpath).click()

# if __name__ == "__main__":
# 	user = UserLogin()
# 	# user.accept_permissions()
# 	# user.click_sign_in_button()
# 	# user.enter_user_email()
# 	# user.enter_user_password()
# 	# user.click_login_in_button()
# 	# user.ignore_post_login_popups()
# 	# user.click_menu_sidebar()
# 	# user.buy_subscription()

# Billing: //android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/material_drawer_name' and @text='Billing']

	# time.sleep(4)
	# print("App launched successfully!")

