from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://katalon-demo-cura.herokuapp.com/profile.php#login')
        self.username_field = self.browser.find_element(By.ID,'txt-username')
        self.password_field = self.browser.find_element(By.ID,'txt-password')
        self.login_button = self.browser.find_element(By.ID,'btn-login')

    def validate_login_page(self):
        assert '#login' in self.browser.current_url, 'Not on the Login page'

    def input_username(self, username):
        self.username_field.send_keys(username)

    def input_password(self, password):
        self.password_field.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def verify_appointment_page_is_opened(self):
        assert '#appointment' in self.browser.current_url, 'Not on the Appointment page'

    def verify_error_message(self):
        self.browser.find_element(By.XPATH,"//p[contains(text(), 'Login failed! Please ensure the username and password are valid.')]")