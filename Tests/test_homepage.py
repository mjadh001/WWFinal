from Pages.HomePage import HomePage
from Tests.test_base import BaseTest
from Config.config import TestData


class Test_HomePage(BaseTest):

    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        actual_title = self.homePage.get_home_page_title()
        assert actual_title == TestData.HOME_PAGE_TITLE, "Title does not match"

    def test_display_location_distance(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_studio_icon()
        self.homePage.enter_location(TestData.ZIPCODE)
        self.homePage.click_search()
        result_loc = self.homePage.verify_location_result()
        print("\nLocation : ", result_loc)
        result_dist = self.homePage.verify_distance_result()
        print("\nDistance : ", result_dist)
