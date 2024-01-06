from Pages.BasePage import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fb_login(self, email, password):
        self.fill( "email_XPATH", email)
        self.fill( "password_XPATH", password)
        self.click("login_button_XPATH")