from Project_WOLT.globals import URL
from Project_WOLT.pages.discovery_page import DiscoveryPage
from Project_WOLT.pages.restaurants_page import RestaurantsPage
from Project_WOLT.pages.welcome_page import WelcomePage


class TestMain():


    def test_main(self,setup_playwright_project_wolt):
        page = setup_playwright_project_wolt
        page.goto(URL)
        allow_cookies_button = page.locator("[data-test-id='allow-button']")
        allow_cookies_button.click()

        welcome_page = WelcomePage(page)
        welcome_page.search_for_item("petah tikva")
        welcome_page.test_result_list()

        discovery_page = DiscoveryPage(page)
        discovery_page.go_to_restaurants()

        restaurants_page = RestaurantsPage(page)
        restaurants_page.most_places_test()

