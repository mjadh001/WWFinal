import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StudioPage:

    RESULT_DISPLAYED_STUDIO = "//h1[@class = 'locationName-1jro_']"
    BH_DROPDOWN = "//*[name()='svg' and @class = 'hoursIcon-II-H2']"
    RESULT_BUSINESS_HOURS = "//div[@class = 'hoursWrapper-1KHIv show-1db4o']"

    def __init__(self, driver):
        self.driver = driver

    """Page Actions for Studio Page"""

    """This method is used to get the text displayed after clicking on the first searched result"""
    def verify_studio_page_text(self):
        return self.driver.find_element(By.XPATH, self.RESULT_DISPLAYED_STUDIO).text

    """This method is used to click on the arrow to expand Business Hours Menu"""
    def click_business_hour_dropdown(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.BH_DROPDOWN)))
        self.driver.find_element(By.XPATH, self.BH_DROPDOWN).click()

    """This method is used to get all the Business hours"""
    def get_business_hours(self):
        self.result_hours = []
        time.sleep(5)
        self.result_hours = self.driver.find_elements(By.XPATH, self.RESULT_BUSINESS_HOURS)
        return self.result_hours







