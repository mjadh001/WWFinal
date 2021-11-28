import time

from Pages.HomePage import HomePage
from Pages.StudioPage import StudioPage
from Tests.test_base import BaseTest


class Test_StudioPage(BaseTest):

    def test_studio_page_display(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_studio_icon()
        self.homePage.enter_location("10011")
        self.homePage.click_search()
        result_loc = self.homePage.verify_location_result()
        self.homePage.click_location_result()
        self.studioPage = StudioPage(self.driver)
        displayed_studio_result = self.studioPage.verify_studio_page_text()
        assert result_loc == displayed_studio_result, "Mismatch in the displayed location name and first searched " \
                                                      "result "

    def test_business_hours(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_studio_icon()
        self.homePage.enter_location("10011")
        self.homePage.click_search()

        self.homePage.click_location_result()
        self.studioPage = StudioPage(self.driver)
        self.studioPage.click_business_hour_dropdown()

        result_hours = self.studioPage.get_business_hours()
        for hr in result_hours:
            print(f"\n", hr.text)
