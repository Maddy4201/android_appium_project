from pages.login_page import UserLogin


class TestUserLogin:

	def test_user_login(self):
		user = UserLogin()
		user.accept_permissions()
		user.click_sign_in_button()
		user.enter_user_email()
		user.enter_user_password()
		user.click_login_in_button()
		user.ignore_post_login_popups()
		user.click_menu_sidebar()
		user.buy_subscription()





