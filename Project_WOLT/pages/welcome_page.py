from playwright.sync_api import expect


class WelcomePage():

    def __init__(self, page):
        self.page = page


    def search_for_item(self,item:str):
        search_menu= self.page.locator("[id='_R_tdj_']")
        search_menu.click()
        search_menu.fill(item)
        self.page.keyboard.press("Enter")

    def test_result_list(self):
        result_list = self.page.locator("[id='_R_b5cuemq_-list']")
        expect(result_list).to_have_count(1)

        first_item = result_list.locator("li").first
        expect(first_item).to_have_count(1)

        first_item_details = first_item.locator("div").nth(1)
        first_item_name = first_item_details.locator("div").nth(0)
        first_item_country = first_item_details.locator("div").nth(1)
        expect(first_item_name).to_have_text("Petah Tikva")
        expect(first_item_country).to_have_text("Israel")

        first_item.click()