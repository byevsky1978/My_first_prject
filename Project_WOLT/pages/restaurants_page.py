from playwright.sync_api import expect


class RestaurantsPage():

    def __init__(self, page):
        self.page = page

    def test_subtitle(self):
        main_discovery_content = self.page.locator("[data-test-id='MainDiscoveryContent']")
        subtitle = main_discovery_content.locator("h2").first
        expect(subtitle).to_have_text("I feel like eating..")

    def test_most_places(self):
        main_discovery_content = self.page.locator("[data-test-id='MainDiscoveryContent']")
        category_list = main_discovery_content.locator("ul").first
        expect(category_list).to_have_count(1)

        categories = category_list.locator("li")
        most_places_category = None
        most_places = 0
        for category in categories.all():
            category.scroll_into_view_if_needed()
            title = category.locator("h3").first
            subtitle = category.locator("p").first
            expect(subtitle).to_have_count(1)
            count = int(subtitle.text_content().split(" ")[0])
            if count > most_places:
                most_places = count
                most_places_category = title.text_content()

        assert most_places_category == 'Kosher'