from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AppointmentPage:
    def __init__(self, browser):
        self.browser = browser
        self.facility = None
        self.visit_date = None
        self.chk_readmission = False
        self.health_care = None
        self.comment = None
        
    def select_facility(self, facility):
        facility_selector = self.browser.find_element(By.ID,'combo_facility')
        facility_selector = Select(facility_selector)
        facility_selector.select_by_visible_text(facility)
        self.facility = facility

    def check_hospital_readmission(self):
        chk_hospotal_readmission = self.browser.find_element(By.ID,'chk_hospotal_readmission')
        chk_hospotal_readmission.click()
        self.chk_readmission = True

    def check_health_care_radio_button(self, health_care_program):
        health_care_radio_button = None
        if health_care_program == "Medicaid":
            health_care_radio_button = self.browser.find_element(By.ID,'radio_program_medicaid')
        elif health_care_program == "Medicare":
            health_care_radio_button = self.browser.find_element(By.ID,'radio_program_medicare')
        elif health_care_program == "None":
            health_care_radio_button = self.browser.find_element(By.ID,'radio_program_none')
        else:
            raise ValueError(f"Invalid health care program: {health_care_program}")
        self.health_care = health_care_program
        health_care_radio_button.click()

    def set_visit_date(self, date):
        appointment_date_field = self.browser.find_element(By.ID,'txt_visit_date')
        appointment_date_field.send_keys(date)
        self.visit_date = date

    def set_comments(self, comment):
        comment_field = self.browser.find_element(By.ID,'txt_comment')
        comment_field.send_keys(comment)
        self.comment = comment

    def click_book_appointment_button(self):
        book_appointment_button = self.browser.find_element(By.ID,'btn-book-appointment')
        book_appointment_button.click()

    def verify_appointment_confirmation(self):
        chk_readmission = "Yes" if self.chk_readmission else "No"
        self.browser.find_element(
            By.XPATH,
            "//div/*[normalize-space(text()) = 'Appointment Confirmation']"
        )
        self.browser.find_element(
            By.XPATH,
            f"//div[//*[normalize-space(text()) = 'Facility'] and //*[normalize-space(text()) = '{self.facility}'] and count(*)=2]"
        )
        self.browser.find_element(
            By.XPATH,
            f"//div[//*[normalize-space(text()) = 'Apply for hospital readmission'] and //*[normalize-space(text()) = '{chk_readmission}'] and count(*)=2]"
        )
        self.browser.find_element(
            By.XPATH,
            f"//div[//*[normalize-space(text()) = 'Healthcare Program'] and //*[normalize-space(text()) = '{self.health_care}'] and count(*)=2]"
        )
        self.browser.find_element(
            By.XPATH,
            f"//div[//*[normalize-space(text()) = 'Visit Date'] and //*[normalize-space(text()) = '{self.visit_date}'] and count(*)=2]"
        )
        self.browser.find_element(
            By.XPATH,
            f"//div[//*[normalize-space(text()) = 'Comment'] and //*[normalize-space(text()) = '{self.comment}'] and count(*)=2]"
        )