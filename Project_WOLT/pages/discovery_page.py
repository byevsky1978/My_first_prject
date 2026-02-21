from playwright.sync_api import expect


class DiscoveryPage():

    def __init__(self, page):
        self.page = page


    def go_to_restaurants(self):
        category_list = self.page.locator("[data-test-id='ProductLine.Grid']").first
        expect(category_list).to_have_count(1)

        li_restaurants = category_list.locator("li", has_text="Restaurants").first
        expect(li_restaurants).to_have_count(1)

        li_restaurants.click()