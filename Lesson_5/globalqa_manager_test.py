class Test_Globalqa():

    def test_global(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        login_manager = page.locator("[class='btn btn-primary btn-lg']")
        login_manager.click()


