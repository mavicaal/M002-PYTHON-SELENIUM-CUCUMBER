from selenium.webdriver.common.by import By
import time

class AppointmentPage:
    def __init__(self, browser):
        self.browser = browser
        self.facility_selector = self.browser.find_element(By.ID,'combo_facility')
        self.chk_hospotal_readmission = self.browser.find_element(By.ID,'chk_hospotal_readmission')
       
    def verify_appointment_page_is_opened(self):
        time.sleep(5)
        assert '#appointment' in self.browser.current_url, 'Not on the Appointment page'