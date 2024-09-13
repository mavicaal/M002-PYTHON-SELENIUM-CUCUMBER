from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.username_field = self.browser.find_element(By.ID,'txt-username')
        self.password_field = self.browser.find_element(By.ID,'txt-password')
        self.login_button = self.browser.find_element(By.ID,'btn-login')

    def navigate_to_login_page(self):
        self.browser.get('https://katalon-demo-cura.herokuapp.com/profile.php#login')

    def input_username(self, username):
        self.username_field.send_keys(username)

    def input_password(self, password):
        self.password_field.send_keys(password)

    def click_login_button(self):
        self.login_button.click()