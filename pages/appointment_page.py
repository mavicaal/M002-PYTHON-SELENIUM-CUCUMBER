from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AppointmentPage:
    def __init__(self, browser):
        self.browser = browser
        
    def select_facility(self, facility):
        self.facility_selector = self.browser.find_element(By.ID,'combo_facility')
        self.facility_selector = Select(self.facility_selector)
        self.facility_selector.select_by_visible_text(facility)

    def check_hospital_readmission(self):
        self.chk_hospotal_readmission = self.browser.find_element(By.ID,'chk_hospotal_readmission')
        self.chk_hospotal_readmission.click()

    def check_health_care_radio_button(self):
        self.health_care_radio_button = self.browser.find_element(By.ID,'radio_program_medicaid')
        self.health_care_radio_button.click()
    