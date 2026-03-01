from playwright.sync_api import expect

from Project_WOLT.globals import URL
from Project_WOLT.pages.discovery_page import DiscoveryPage
from Project_WOLT.pages.restaurants_page import RestaurantsPage
from Project_WOLT.pages.welcome_page import WelcomePage


class TestMain():
    def test_cookies(self, setup_playwright_project_wolt):
        page = setup_playwright_project_wolt
        allow_cookies_button = page.locator("[data-test-id='allow-button']")
        expect(allow_cookies_button).to_have_count(1)
        allow_cookies_button.click()

    def test_welcome_page(self, setup_playwright_project_wolt):
        page = setup_playwright_project_wolt
        welcome_page = WelcomePage(page)
        welcome_page.search_for_item("petah tikva")
        welcome_page.test_result_list()

    def test_discovery_page(self, setup_playwright_project_wolt):
        page = setup_playwright_project_wolt
        discovery_page = DiscoveryPage(page)
        discovery_page.go_to_restaurants()

    def test_restaurants_page_subtitle(self, setup_playwright_project_wolt):
        page = setup_playwright_project_wolt
        restaurants_page = RestaurantsPage(page)
        restaurants_page.test_subtitle()

    def test_restaurants_page_most_places(self, setup_playwright_project_wolt):
        page = setup_playwright_project_wolt
        restaurants_page = RestaurantsPage(page)
        restaurants_page.test_most_places()

