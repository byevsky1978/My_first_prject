from playwright.sync_api import expect


class RestaurantsPage():

    def __init__(self, page):
        self.page = page


    def most_places_test(self):
        main_discovery_content = self.page.locator("[data-test-id='MainDiscoveryContent']")
        category_list = main_discovery_content.locator("ul").first
