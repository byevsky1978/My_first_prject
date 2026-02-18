from Project_WOLT.globals import URL
from Project_WOLT.pages.welcome_page import WelcomePage


class TestMain():
    def test_main(self,setup_playwright_project_wolt):
        page = setup_playwright_project_wolt
        page.goto(URL)
        welcome_page = WelcomePage(page)
        welcome_page.search_for_item("petah tikva")
        page.pause()




        print('CHECK')


