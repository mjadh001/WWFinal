from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Config.config import TestData


class HomePage:
    STUDIO_EL = "//button[@class = 'toggleButton-2ikVW']"
    LOCATION_EL = "//input[@id = 'location-search']"
    SEARCH_EL = "//button[@class = 'ww button primary cta-1JqRp']"
    RESULT_LOCATION_EL = "//div[@class = 'linkContainer-1NkqM']"
    RESULT_DISTANCE_EL = "//span[@class = 'distance-OhP63']"

    def __init__(self, driver):
        self.driver = driver

        self.driver.get(TestData.BASE_URL)

    """Page Actions for Home Page"""

    """This method is used to get title of the page"""

    def get_home_page_title(self):
        return self.driver.title

    """This method is used to click on the Studio element"""

    def click_studio_icon(self):
        click_studio = self.driver.find_elements(By.XPATH, self.STUDIO_EL)
        click_studio[1].click()

    """This method is used to enter text in the textbox of the page"""

    def enter_location(self, zipcode):
        self.driver.find_element(By.XPATH, self.LOCATION_EL).send_keys(zipcode)

    """This method is used to click on the search button of the page"""

    def click_search(self):
        self.driver.find_element(By.XPATH, self.SEARCH_EL).click()

    """This method is used to read the text of the search results"""

    def location_result(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.RESULT_LOCATION_EL)))
        return self.driver.find_element(By.XPATH, self.RESULT_LOCATION_EL)

    """This method is used to read the location text results"""
    def verify_location_result(self):
        loc_res = self.location_result()
        return loc_res.text

    """This method is used to read the distance text results"""
    def verify_distance_result(self):
        return self.driver.find_element(By.XPATH, self.RESULT_DISTANCE_EL).text

    """This method is used to click on the first link location result"""
    def click_location_result(self):
        loc_res = self.location_result()
        return loc_res.click()
