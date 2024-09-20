from selenium.webdriver.common.by import By


class AppointmentPage:
    def __init__(self, browser):
        self.browser = browser
        self.facility_selector = self.browser.find_element(By.ID,'combo_facility')
        self.chk_hospotal_readmission = self.browser.find_element(By.ID,'chk_hospotal_readmission')