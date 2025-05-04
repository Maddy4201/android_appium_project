from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy

# Define capabilities using AppiumOptions
from appium.options.android import UiAutomator2Options

from pages.base_page import BasePage


class SignUpUser(BasePage):

    permission_popup_xpath = "//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/btn_ok']"
    location_popup_xpath = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"
    allow_call_popup_xpath = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"
    register_button_xpath = "//android.widget.TextView[@resource-id='in.co.websites.websitesapp:id/btn_register']"
    full_name_field_xpath = "//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/fullname']"
    phone_no_field_xpath = "//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/phone']"
    email_field_xpath = "//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/email_reg']"
    password_field_xpath = "//android.widget.EditText[@resource-id='in.co.websites.websitesapp:id/password']"
    sign_up_button_xpath = "//android.widget.Button[@resource-id='in.co.websites.websitesapp:id/email_register_button']"


    def __init__(self):
        super().__init__()

    def sign_up_flow(self):
        # Wait for app to launch
        # time.sleep(3)
        element = self.driver.find_element(AppiumBy.XPATH, self.permission_popup_xpath)
        element.click()
        self.driver.find_element(AppiumBy.XPATH, self.location_popup_xpath).click()
        self.driver.find_element(AppiumBy.XPATH, self.allow_call_popup_xpath).click()
        self.driver.find_element(AppiumBy.XPATH, self.register_button_xpath).click()
        self.driver.find_element(AppiumBy.XPATH, self.full_name_field_xpath).send_keys("Test User09")
        self.driver.find_element(AppiumBy.XPATH, self.phone_no_field_xpath).send_keys("98767364")
        self.driver.find_element(AppiumBy.XPATH, self.email_field_xpath).send_keys("testemail123@ymail.com")
        self.driver.find_element(AppiumBy.XPATH, self.password_field_xpath).send_keys("Test@12345")
        self.driver.find_element(AppiumBy.XPATH, self.sign_up_button_xpath).click()

if __name__ == "__main__":
    test = SignUpUser()
    test.sign_up_flow()


# # Sign up flow X-paths


# show_password_icon = "//android.widget.ImageButton[@content-desc='Show password']"
#
# countrycode_search_field = "//android.widget.AutoCompleteTextView[@resource-id='in.co.websites.websitesapp:id/search_src_text']"
# # enter only the country code number into the above field
#
# the box which has searched phone codes = //androidx.recyclerview.widget.RecyclerView[@resource-id="in.co.websites.websitesapp:id/recycler_phonecode"]
# list of no displayed x path = (//android.widget.LinearLayout[@resource-id="in.co.websites.websitesapp:id/ll_language"])[1]
#
# google_signup_logo = "//android.widget.ImageButton[@content-desc='Google']"
# facebook_signup_logo = "//android.widget.ImageButton[@content-desc='Facebook']"
#
# gmail_id_container_list = "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.gms:id/list']"
# add_another_gmail_account_option = "//android.widget.TextView[@resource-id='com.google.android.gms:id/add_account_chip_title']"
